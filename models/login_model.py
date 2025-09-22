from pydantic import BaseModel
from beanie import Document

class User(BaseModel):
    email: str
    password: str


class LoginModel(Document):
    full_name:str=''
    email: str
    hashed_password: str
    phone_number: str=''
    class Config:
        orm_mode = True
    class Settings:
        name = "users"