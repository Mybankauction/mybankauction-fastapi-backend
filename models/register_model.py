from beanie import Document
from typing import Optional
from pydantic import BaseModel


class Register(BaseModel):
   full_name:str
   email:str
   password:str

class RegisterDb(Document):
    full_name: str
    email: str
    hashed_password: str
    class Settings:
        name = "users"