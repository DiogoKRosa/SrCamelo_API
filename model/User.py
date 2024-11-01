from model.database import db
import bson.json_util as json_util


collection = db['users']

class User:
    def __init__(self, data):
        self.data = data

    async def insert_one(self):
        collection.insert_one(self.data)

async def get_users():
    res = collection.find({})
    return json_util.dumps(res)