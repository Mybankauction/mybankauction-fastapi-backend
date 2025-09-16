from beanie import Document
class InterestedModel(Document):
    user_id:str
    properties:list[str]

    class Settings():
        name= "interested_users"