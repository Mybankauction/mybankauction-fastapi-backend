import os
import sys
from dotenv import load_dotenv
load_dotenv()
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.properties_model import Property
from models.register_model import RegisterDb
from models.login_model import LoginModel


async def init_db():
    try:
        client = AsyncIOMotorClient(os.getenv("DATABASE_URL"))
        database = client.Zbot
        await init_beanie(database=database, document_models=[Property,RegisterDb,LoginModel])
        print("Database initialized")
    except Exception as e:
        print("Database initialization failed", e)
        sys.exit(1)