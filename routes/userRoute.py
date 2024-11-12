from fastapi import APIRouter, HTTPException, status, Response
from model.User import User, get_users
from model.ApiResponse import APIResponse
from pydantic import BaseModel
from auth.authentication import get_password_hash

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

@router.post('/users')
async def create_user(user: UserModel):
    try:
        print(user)
        user.password = get_password_hash(user.password)
        new_user = User(user.dict())
        response = await new_user.insert_one()
        return APIResponse(
            status=status.HTTP_201_CREATED,
            message="Usuario criado com sucesso!",
            data = response
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")

@router.get('/users')
async def get_all_users():
    try:
        users = await get_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
