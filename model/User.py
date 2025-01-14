from model.database import db
from bson import json_util
from bson.objectid import ObjectId
import json

collection = db['users']

class User:
    def __init__(self, data):
        self.data = data

    async def insert_one(self):
        sid = collection.insert_one(self.data).inserted_id
        object = collection.find_one({"_id": sid})
        return json.loads(json_util.dumps(object))

async def get_users():
    res = collection.find({})
    return json.loads(json_util.dumps(res))

async def get_user_by_email(email):
    res = collection.find_one({"email": email})
    return json.loads(json_util.dumps(res))

async def get_user_by_id(id):
    res = collection.find_one({"_id": ObjectId(id)})
    return json.loads(json_util.dumps(res))

async def update_new_vendor_banner(id, data):
    print(id, data)
    res = collection.update_one({"_id": ObjectId(id)}, 
                                {"$set": {
                                    "image": data["imageBanner"], 
                                    "establishment": data["fantasyName"], 
                                    "paymentMethods": data["paymentMethods"]
                                    }
                                })
    object = collection.find_one({"_id": ObjectId(id)})
    return json.loads(json_util.dumps(object))

async def update_first_access(id):
    res = collection.update_one({"_id": ObjectId(id)}, {"$set": {"firstAccess": False}})
    object = collection.find_one({"_id": ObjectId(id)})
    return json.loads(json_util.dumps(object))