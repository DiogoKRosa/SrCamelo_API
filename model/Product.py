from model.database import db
from bson import json_util
from bson.objectid import ObjectId
import json

collection = db['products']

class Product:
    def __init__(self, data):
        self.data = data

    async def insert_one(self):
        sid = collection.insert_one(self.data).inserted_id
        object = collection.find_one({"_id": sid})
        return json.loads(json_util.dumps(object))

async def get_products(vendor_id):
    res = collection.find({"vendor_id": vendor_id})
    return json.loads(json_util.dumps(res))

async def update_product(id, data):
    res = collection.update_one({"_id": ObjectId(id)}, {"$set": {
        "name": data['name'],
        "description": data['description'],
        "price": data['price'],
        "image": data['image'],
        "category": data['category']
    }})
    object = collection.find_one({"_id": ObjectId(id)})
    return json.loads(json_util.dumps(object))

async def delete_product(id):
    res = collection.delete_one({"_id": ObjectId(id)})
    