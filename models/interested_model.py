from beanie import Document
from pydantic import BaseModel, field_validator


class InterestedModel(Document):
    user_id:str
    properties:list[str]

    class Settings():
        name= "interested_users"


class Interested(BaseModel):
    property_id:str
