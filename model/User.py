from model.database import db


collection = db['users']

class User:
    def __init__(self, data):
        self.data = data

    async def insert_one(self):
        collection.insert_one(self.data)