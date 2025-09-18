from beanie import Document
from pydantic import BaseModel, field_validator, ValidationError


class InterestedModel(Document):
    user_id:str
    properties:list[str]
    phone_number:str

    class Settings():
        name= "interested_users"


class Interested(BaseModel):
    property_id:str
    phone_number:str=""

    @field_validator("phone_number")
    def validate_phone_number(cls,phone_number:str):
        print("validate_phone_number")
        if phone_number != '':
            if len(phone_number) != 10:
                raise ValueError("Phone number must be exactly 10 digits")
        return phone_number
