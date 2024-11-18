from fastapi import UploadFile, File
from fastapi import APIRouter, HTTPException, status, Response, Form
from model.Product import Product, get_products, update_product, delete_product
from model.ApiResponse import APIResponse
from pydantic import BaseModel
import json
import os 
import uuid

router = APIRouter()

class ProductModel(BaseModel):
    vendor_id: str | None = None
    name: str | None = None
    price: float | None = None
    description: str | None = None
    category: str | None = None

@router.post('/products')
async def createProduct(product: str = Form(...), image: UploadFile | None = File(None)):
    try:
        product_data = json.loads(product)

        if image:
            file_extension = os.path.splitext(image.filename)[1] 
            unique_filename = f"{uuid.uuid4()}{file_extension}"
            file_location = os.path.join("uploads" , unique_filename)
            with open(file_location, "wb") as buffer:
                buffer.write(image.file.read())
            product_data['image'] = file_location

        new_product = Product(product_data)
        response = await new_product.insert_one()
        return APIResponse(
            status=status.HTTP_201_CREATED,
            message="Produto criado com sucesso!",
            data = response
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")

@router.get('/products/{vendor_id}')
async def get_products_from_vendor(vendor_id: str):
    try:
        products = await get_products(vendor_id)
        print(products)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    
@router.put('/products/{id}')
async def update_produt(product: str = Form(...), image: UploadFile | None = File(None)):
    try:
        product_data = json.loads(product)
        print(product_data)
        if image:
            file_extension = os.path.splitext(image.filename)[1] 
            unique_filename = f"{uuid.uuid4()}{file_extension}"
            file_location = os.path.join("uploads" , unique_filename)
            with open(file_location, "wb") as buffer:
                buffer.write(image.file.read())
            product_data['image'] = file_location
        print(product_data)
        response = await update_product(product_data['_id']['$oid'], product_data)
        print(response)
        return APIResponse(
            status=status.HTTP_202_ACCEPTED,
            message="Produto atualizado com sucesso!",
            data = response
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    
@router.delete('/products/{id}')
async def delete_product_handler(id: str):
    try:
        response = await delete_product(id)
        return APIResponse(
            status=status.HTTP_202_ACCEPTED,
            message="Produto deletado com sucesso!"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")