from model.database import db
from bson import json_util
from bson.objectid import ObjectId
import json

collection = db['coordinates']

class Coordinate:
    def __init__(self, data):
        self.data = data
    
    async def insert_one(self):
        sid = collection.insert_one(self.data).inserted_id
        object = collection.find_one({"_id": sid})
        return json.loads(json_util.dumps(object))

async def get_all():
    res = collection.find()
    return json.loads(json_util.dumps(res))

async def get_all_vendors():
     res = collection.find({"user_type": "vendedor"})
     return json.loads(json_util.dumps(res))

async def get_one(user_id):
    res = collection.find({"user_id": user_id})
    return json.loads(json_util.dumps(res))

def update_one(user_id, latitude, longitude):
    obj = collection.find_one({"userId": user_id})
    if obj != None:
        res = collection.update_one(
            {"userId": user_id},
            {"$set": {
                
                "latitude": latitude,
                "longitude": longitude
            }},
            upsert=True
        )
    else:
        res = collection.insert_one({
            "userId": user_id,
            "latitude": latitude,
            "longitude": longitude
        })
    
    
    
