from fastapi import APIRouter, HTTPException, status, Response
from model.Product import Product, get_products, update_product, delete_product
from model.ApiResponse import APIResponse
from pydantic import BaseModel

router = APIRouter()

class ProductModel(BaseModel):
    vendor_id: str | None = None
    name: str | None = None
    price: float | None = None
    description: str | None = None
    category: str | None = None
    image: str | None = None

@router.post('/products')
async def createProduct(product: ProductModel):
    try:
        print(product)
        new_product = Product(product.dict())
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
        return APIResponse(
            status=status.HTTP_202_ACCEPTED,
            message="Produtos retornados",
            data = products
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    
@router.put('/products/{id}')
async def update_produt(id: str, product: ProductModel):
    try:
        response = await update_product(id, product.dict())
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