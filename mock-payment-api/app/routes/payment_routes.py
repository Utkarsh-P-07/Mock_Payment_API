from typing import List

from fastapi import APIRouter, HTTPException, status

from ..models.payment import PaymentCaptureRequest, PaymentPublic
from ..services import capture_payment, list_payments

router = APIRouter()


@router.post("/capture", response_model=PaymentPublic, status_code=status.HTTP_201_CREATED)
async def capture_payment_endpoint(payload: PaymentCaptureRequest):
    """
    Mimics Razorpay capture API.
    """
    payment = await capture_payment(payload)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return PaymentPublic(**payment.dict(by_alias=False))


@router.get("", response_model=List[PaymentPublic])
async def list_payments_endpoint(limit: int = 20):
    payments = await list_payments(limit=limit)
    return [PaymentPublic(**p.dict(by_alias=False)) for p in payments]


