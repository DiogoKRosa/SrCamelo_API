from fastapi import APIRouter, HTTPException, status, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from auth.authentication import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from model.User import get_user_by_email
from model.ApiResponse import APIResponse
from datetime import timedelta

router = APIRouter()

class LoginModel(BaseModel):
    email: str | None = None
    password: str | None = None

@router.post("/login")
async def login(form_data: LoginModel):
    print(form_data)
    user = await get_user_by_email(form_data.email)
    print(user)
    if not user or not verify_password(form_data.password, user['password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario ou Senha Incorreta",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["name"]}, expires_delta=access_token_expires
    )
    return APIResponse(
        status=status.HTTP_200_OK,
        message="Login realizado com sucesso!",
        data={"access_token": access_token, "token_type": "bearer", "userType": user["userType"], "user_id": user["_id"]["$oid"], "firstAccess": user["firstAccess"] },
    )