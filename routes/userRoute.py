from fastapi import APIRouter, HTTPException, status
from model.User import User, get_users
from pydantic import BaseModel
import json

router = APIRouter()

class UserModel(BaseModel):
    userType: str | None = None
    name: str | None = None
    cpf: str | None = None
    email: str | None = None
    telephone: str | None = None
    password: str | None = None
    country: str | None = None
    uf: str | None = None
    city: str | None = None

@router.post('/users', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserModel):
    try:
        user_dict = user.dict()
        new_user = User(user_dict)
        result = await new_user.insert_one()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")

@router.get('/users')
async def get_all_users():
    try:
        users = await get_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
