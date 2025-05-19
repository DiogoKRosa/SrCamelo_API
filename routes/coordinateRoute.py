from fastapi import APIRouter, HTTPException, status, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from model.Coordinate import Coordinate, get_all_vendors, get_one, update_one, get_all
from model.User import get_user_by_id
from model.ApiResponse import APIResponse
from datetime import timedelta

class CoordinateModel(BaseModel):
    userId: str
    latitude: float
    longitude: float

router = APIRouter()

@router.get("/location")
async def get_all_coordinate():
    try:
        coord = await get_all()
        for register in coord:
            del register['_id']
            user = await get_user_by_id(register['userId'])
            register['userName'] = user['name']

        return APIResponse(
            status=status.HTTP_202_ACCEPTED, message="OK", data=coord
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro: {e}")
    
@router.post("/location")
async def update_coordinate(data: CoordinateModel):
    try:
        res = update_one(data.userId, data.latitude, data.longitude)
        return APIResponse(
            status=status.HTTP_200_OK,
            message="Coordenada atualizada com sucesso"
        )
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar valor de coordenada: {e}")