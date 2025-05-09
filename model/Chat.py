from model.database import db
from bson import json_util
from bson.objectid import ObjectId
import json
from pymongo import DESCENDING

collection = db['chat']

class Chat:
    def __init__(self,data):
        self.data = data
    
    async def insert_one(self):
        sid = collection.insert_one(self.data).inserted_id
        object = collection.find_one({"_id": sid})
        return json.loads(json_util.dumps(object))

async def get_all_last_messages(loginId: str):
    pipeline = [
        {"$match": {"participants": loginId}},
        
        # Transforma a lista de participantes em uma string ordenada (para tratar pares únicos)
        {"$addFields": {
            "participant_key": {
                "$reduce": {
                    "input": { "$sortArray": {"input": "$participants", "sortBy": 1} },
                    "initialValue": "",
                    "in": {
                        "$cond": [
                            { "$eq": ["$$value", ""] },
                            "$$this",
                            { "$concat": ["$$value", "_", "$$this"] }
                        ]
                    }
                }
            }
        }},

        # Ordena do mais recente para o mais antigo
        {"$sort": {"datetime": -1}},

        # Agrupa por chave única de participantes e pega o mais recente
        {"$group": {
            "_id": "$participant_key",
            "latest_message": { "$first": "$$ROOT" }
        }},

        {"$sort": {"latest_message.datetime": -1}}
    ]

    result = collection.aggregate(pipeline)
    raw_data = [doc["latest_message"] for doc in result]
    return json.loads(json_util.dumps(raw_data))

async def get_all_private_messages(loginId, userId):
    res = collection.find({"participants": {"$all": [loginId, userId] }}).sort("datetime", 1)
    return json.loads(json_util.dumps(res))
