from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017/"
try:
    client = MongoClient(MONGO_URI)
    db = client["srcamelo"]

except Exception as e:
    raise Exception(
        "Houve um problema:", e
    )
