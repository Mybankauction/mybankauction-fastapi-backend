from pydantic import BaseModel
from beanie import Document

class User(BaseModel):
    email: str
    password: str


class LoginModel(Document):
    email: str
    hashed_password: str
    class Settings:
        name = "users"