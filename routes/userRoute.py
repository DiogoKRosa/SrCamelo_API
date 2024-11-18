from fastapi import APIRouter, HTTPException, status, Response, UploadFile, File, Form
from model.User import User, get_users, update_new_vendor_banner
from model.ApiResponse import APIResponse
from pydantic import BaseModel
from auth.authentication import get_password_hash
import json
import os
import uuid

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
    image: str | None = None
    establishment: str | None = None

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

@router.put('/newVendor/{vendor_id}')
async def addEstablishment(bannerFormVendor:str = Form(...), image: UploadFile | None = File(None)):
    try:
        form_data = json.loads(bannerFormVendor)
        
        if image:
            file_extension = os.path.splitext(image.filename)[1] 
            unique_filename = f"{uuid.uuid4()}{file_extension}"
            file_location = os.path.join("uploads" , unique_filename)
            with open(file_location, "wb") as buffer:
                buffer.write(image.file.read())
            form_data['imageBanner'] = file_location
        
        print(form_data)

        response = await update_new_vendor_banner(form_data['_id']['$oid'] , form_data)

        return APIResponse(
            status=status.HTTP_202_ACCEPTED,
            message="Banner atualizado com sucesso!",
            data = response
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")

