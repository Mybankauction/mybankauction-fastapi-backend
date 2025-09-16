from models.interested_model import InterestedModel

async def push_interested_property(user_id, property_id):
    try:
        interested = InterestedModel(user_id=user_id,properties=[property_id])
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
            await interested.save()
            return {"status_code": 201, "message": "property successfully added to Interested List"}

    except Exception as e:
        print("Error happened at push_interested_property", e)
        return {"status_code": 500, "message": "Internal server error"}


