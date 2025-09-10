from  datetime import datetime
from models.properties_model import Property
from utility.date_formater import parse_date
async def get_properties(page) -> list:
     properties_list = []
     page_limit = 10

     try:
         skip = (page - 1) * page_limit
         properties = (
             await Property.find_all()
             .sort("-_id")  # newest first
             .skip(skip)  # skip (page-1)*PAGE_SIZE
             .limit(page_limit)  # take PAGE_SIZE documents
             .to_list()
         )
         count = await Property.find_all().count()
         pagination = (count + page_limit- 1) // 10

         for prop in properties:
             pro = prop.model_dump(by_alias=True)  # convert Beanie Document → dict
             pro["_id"] = str(pro["_id"])
             # Safely format dates
             if isinstance(pro.get("auction_start_date"), datetime):
                 pro["auction_start_date"] = pro["auction_start_date"].strftime("%d-%m-%Y %I:%M %p")
             if isinstance(pro.get("auction_end_date"), datetime):
                 pro["auction_end_date"] = pro["auction_end_date"].strftime("%d-%m-%Y %I:%M %p")
             properties_list.append(pro)
             print("This is the type",type(pro.get("reserve_price")))
             print(pro)


         return {"status": 200, "data": properties_list,"pagination":{"page":page,"total_pages":pagination,"items":count}}
     except Exception as e:
         print("Error in get_properties:", e)
         return {"status": 500, "error": str(e)}


async def filter_properties(filters,page) -> dict:
    limit = 10
    skip_count = (page -1)*limit
    try:
        if filters.get('auction_id') is not None:
            result= await Property.find_one({"Auction Id": filters['auction_id']})
            return {"status": 200, "data": result}
        query = {}
        if filters.get("state"):
            query["State"] = filters["state"]

        if filters.get("city"):
            query["City"] = filters["city"]

        if filters.get("area"):
            query["Area"] = filters["area"]

        if filters.get("property_type"):
            query["Property Type"] = filters["property_type"]
        if filters.get("auction_start_date") or filters.get("auction_end_date"):
            date_filter = {}

            if filters.get("auction_start_date"):
                date_filter["$gte"] = parse_date(filters["auction_start_date"])
            if filters.get("auction_end_date"):
                date_filter["$lte"] = parse_date(filters["auction_end_date"])
            query["auction_start_date"] = date_filter

        # Price range
        if filters.get("min_price") is not None or filters.get("max_price") is not None:
            price_filter = {}
            if filters.get("min_price") is not None:
                price_filter["$gte"] = filters["min_price"]
            if filters.get("max_price") is not None:
                price_filter["$lte"] = filters["max_price"]
            query["Reserve Price"] = price_filter
        # Run the query
        results = await Property.find(query).skip(skip_count).limit(limit).to_list()
        results_dicts = []
        for prop in results:
            data = prop.model_dump(by_alias=True)
            data["_id"] = str(data["_id"])
            for field, value in data.items():
                if isinstance(value, datetime):
                    data[field] = value.isoformat()
            results_dicts.append(data)
        count = await Property.find(query).count()
        pagination = (count + limit-1) // 10
        print(results_dicts)
        return { "status": 200,"data": results_dicts,"pagination": {"page": page,"total_pages": pagination,
        "items": count
    }
}
    except Exception as e:
        print("Error in filter_properties:", e)
        return {"status": 500, "error":"Try after sometime"}
    return {"status": 200, "data": filters}