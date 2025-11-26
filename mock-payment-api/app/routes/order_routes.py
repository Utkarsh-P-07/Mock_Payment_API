from typing import List

from fastapi import APIRouter, HTTPException, Query

from ..models.order import OrderCreate, OrderPublic
from ..services import create_order, get_order, list_orders

router = APIRouter()


@router.post("", response_model=OrderPublic)
async def create_order_endpoint(payload: OrderCreate):
    """
    Razorpay-like create order endpoint.
    """
    order = await create_order(payload)
    return OrderPublic(**order.dict(by_alias=False))


@router.get("/{order_id}", response_model=OrderPublic)
async def get_order_endpoint(order_id: str):
    order = await get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderPublic(**order.dict(by_alias=False))


@router.get("", response_model=List[OrderPublic])
async def list_orders_endpoint(limit: int = Query(20, ge=1, le=100)):
    orders = await list_orders(limit=limit)
    return [OrderPublic(**o.dict(by_alias=False)) for o in orders]


