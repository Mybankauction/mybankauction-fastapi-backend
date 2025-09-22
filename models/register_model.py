from beanie import Document
from typing import Optional
from pydantic import BaseModel,field_validator


class Register(BaseModel):
   full_name:str
   email:str
   password:str
   phone_number:str

@field_validator('phone_number')
def validate_phone_number(cls,phone_number:str):
    print("validate_phone_number")
    if phone_number != '':
        if len(phone_number) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
    return phone_number


class RegisterDb(Document):
    full_name: str
    email: str
    hashed_password: str
    phone_number: str
    class Settings:
        name = "users"