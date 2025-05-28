from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, Field, validator
from model.ApiResponse import APIResponse
from model.Invoice import insert_invoice, get_all_invoices_from_user
from typing import List, Optional
from datetime import datetime

router = APIRouter()

class ProductInvoiceModel(BaseModel):
    productId: str
    productName: str
    productQtd: int
    productPrice: float

class InvoiceModel(BaseModel):
    invoiceStatus: str
    clientId: str
    clientName: str
    clientNumber: str
    vendorId: str
    vendorName: str
    vendorNumber: str
    invoiceTotal: float
    productsList: List[ProductInvoiceModel]
    paymentType: str

@router.post("/invoice")
async def send_invoice(invoice: InvoiceModel):
    try:
        new_invoice = invoice.dict()
        new_invoice['datetime'] = datetime.now()
    
        res = await insert_invoice(new_invoice)
        return APIResponse(
            status=status.HTTP_201_CREATED,
            message="Compra realizada com sucesso",
            data=res
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
    
@router.get("/invoice")
async def get_invoice(uid: str):
    try:
        print(uid)
        res = await get_all_invoices_from_user(uid)

        for invoice in res:
            invoice['datetime'] = invoice['datetime']['$date']

        return APIResponse(
            status=status.HTTP_200_OK,
            message="Requisicao confirmada",
            data=res
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")
