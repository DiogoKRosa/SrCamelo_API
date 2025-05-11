from model.database import db
from bson import json_util
from bson.objectid import ObjectId
import json

collection = db['invoices']

async def insert_invoice(data):
    sid = collection.insert_one(data).inserted_id
    object = collection.find_one({"_id": sid})
    return json.loads(json_util.dumps(object))

async def get_all_invoices_from_user(uid):
    res = collection.find({"$or": [
        {"clientId":uid},
        {"vendorId": uid}
    ]})
    return json.loads(json_util.dumps(res))
