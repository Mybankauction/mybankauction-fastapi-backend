from datetime import datetime

from models.interested_model import InterestedModel
from models.properties_model import Property
from bson import ObjectId
async def push_interested_property(user_id, property_id,phone_number):
    try:
        interested = InterestedModel(user_id=user_id,properties=[property_id],phone_number=phone_number)
        # check if user document already exists
        is_new = await interested.find_one({"user_id": user_id})
        if is_new:
            # update existing document by adding property only if not already present
            if property_id not in is_new.properties:
                result = await is_new.update(
                    {"$addToSet": {"properties": property_id}}
                )
                return {"status_code": 201, "message": "property successfully added to Interested List"}
            else:
                return {"status_code": 200, "message": "property already added to Interested List"}

        else:
            # create a new document for the user
            if phone_number == '':
                return {"status_code": 400, "message": "Phone number not provided"}
            await interested.save()
            return {"status_code": 201, "message": "property successfully added to Interested List"}

    except Exception as e:
        print("Error happened at push_interested_property", e)
        return {"status_code": 500, "message": "Internal server error"}


async def get_interested_property(user_id):
    #check if the user has liked properries or not
    try:
        result_list=list()
        interested = InterestedModel(user_id=user_id,properties=[""],phone_number='')
        is_user_interested_property = await interested.find_one({"user_id": user_id})
        print(is_user_interested_property)
        if is_user_interested_property:
            property_list = is_user_interested_property.properties
            object_ids = [ObjectId(p) for p in property_list]
            properties = await Property.find({"_id": {"$in": object_ids}}).to_list()
            for prop in properties:
                pro = prop.model_dump(by_alias=True)  # convert Beanie Document → dict
                pro["_id"] = str(pro["_id"])
                # Safely format dates
                if isinstance(pro.get("auction_start_date"), datetime):
                    pro["auction_start_date"] = pro["auction_start_date"].strftime("%d-%m-%Y %I:%M %p")
                if isinstance(pro.get("auction_end_date"), datetime):
                    pro["auction_end_date"] = pro["auction_end_date"].strftime("%d-%m-%Y %I:%M %p")
                result_list.append(pro)
            return {"status_code": 200, "message":{"data":result_list}}
        else:
            return {"status_code":200, "message": "No property is added as interested property"}
    except Exception as e:
        print("Error happened at get_interested_property", e)
        return {"status_code": 500, "message": "Internal server error"}
