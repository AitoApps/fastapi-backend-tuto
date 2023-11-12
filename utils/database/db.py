import certifi
from config.settings import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.posts import Post
from models.users import User


# async def init_db():
#     print("init_db", "Begin")
#     client = MongoClient(settings.MONGODB_URI, tlsCAFile=certifi.where())
#     try:
#         client.admin.command("ping")
#         print("[+] Pinged the deployment successfully connected to MongoDB!")
#     except Exception as e:
#         print(e)
#     return client.mydb

async def init_db():
    client = AsyncIOMotorClient(
        settings.MONGODB_URI, tlsCAFile=certifi.where())
    await init_beanie(client.mydb, document_models=[User, Post])
