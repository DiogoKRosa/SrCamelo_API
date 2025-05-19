from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, Field, validator
from model.ApiResponse import APIResponse
from model.Chat import Chat, get_all_last_messages, get_all_private_messages
from model.User import get_user_by_id
from typing import List
from filterWords import filterWords
from datetime import datetime

router = APIRouter()

class ChatModel(BaseModel):
    participants: List[str]
    sender: str
    receiver: str
    message: str
    
    
@router.post("/chat")
async def send_message(message: ChatModel):
    try:
        message_dict = message.dict()
        message_dict['datetime'] = datetime.now()
        newMessage = Chat(message_dict)
        print(message)
        res = await newMessage.insert_one()
        return APIResponse(
            status=status.HTTP_201_CREATED,
            message="Mensagem Enviada com sucesso",
            data=res
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"send_message error: {e}")
    

@router.get('/chat')
async def get_messages(login_id: str):
    try:
        res = await get_all_last_messages(login_id)

        for message in res:
            message['message'] = filterWords(message['message'], 3)
            message['datetime'] = message['datetime']['$date']
            del message['participant_key']

            participant_detail = []
            for participant_id in message['participants']:
                user = await get_user_by_id(participant_id)
                participant_detail.append({
                    "userId": user['_id']['$oid'],
                    "userName": user['name'],
                    "image": user['image']
                })
            message['participantDetails'] = participant_detail
        print(res)
        return APIResponse(
            status=status.HTTP_200_OK,
            message="get_messages = Requisição confirmada",
            data=res
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"get_message error: {e}")
    
@router.get("/chat/{user_id}")
async def get_private_messages(login_id: str, user_id: str):
    try:
        res = await get_all_private_messages(login_id, user_id)
        
        for message in res:
            message['message'] = filterWords(message['message'], 3)
            message['datetime'] = message['datetime']['$date']

        return APIResponse(
            status=status.HTTP_200_OK,
            message="get_private_messages = Requisição confirmada",
            data=res
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"get_message error: {e}")