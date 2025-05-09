from fastapi import APIRouter, HTTPException, status, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from model.Coordinate import Coordinate, get_all_vendors, get_one, update_one
from model.ApiResponse import APIResponse
from datetime import timedelta

class CoordinateModel(BaseModel):
    userId: str
    latitude: float
    longitude: float

router = APIRouter()

@router.get("/coordinate")
async def get_all_coordinate():
    try:
        coord = await get_all_vendors()
        return APIResponse(
            status=status.HTTP_202_ACCEPTED, message="OK", data=coord
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro: {e}")
    
@router.post("coordinate")
async def update_coordinate(data: CoordinateModel):
    try:
        print(data)
    except Exception as e:
        raise APIResponse(status = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar valor de coordenada: {e}")