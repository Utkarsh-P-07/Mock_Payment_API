from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PaymentStatus:
    CREATED = "created"
    CAPTURED = "captured"
    FAILED = "failed"


class PaymentBase(BaseModel):
    order_id: str = Field(..., example="order_123")
    amount: int = Field(..., gt=0, example=50000)
    currency: str = Field("INR", example="INR")
    method: Optional[str] = Field(None, example="card")


class PaymentCaptureRequest(BaseModel):
    order_id: str = Field(..., example="order_123")
    amount: int = Field(..., gt=0, example=50000)
    currency: str = Field("INR", example="INR")


class PaymentInDB(PaymentBase):
    id: str = Field(..., alias="_id")
    status: str = Field(default=PaymentStatus.CREATED)
    captured: bool = False
    created_at: datetime

    class Config:
        allow_population_by_field_name = True


class PaymentPublic(PaymentBase):
    id: str
    status: str
    captured: bool
    created_at: datetime


