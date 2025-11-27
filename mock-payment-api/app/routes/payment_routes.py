from fastapi import APIRouter
from app.controllers.payment_controller import create_payment, update_payment, get_all_payments

payment_router = APIRouter()

@payment_router.post("/")
async def create_mock_payment(data: dict):
    return await create_payment(data)

@payment_router.put("/{order_id}")
async def update_mock_payment(order_id: str, body: dict):
    status = body.get("status")
    return await update_payment(order_id, status)

@payment_router.get("/")
async def fetch_payments():
    return await get_all_payments()
