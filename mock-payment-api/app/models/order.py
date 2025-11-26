from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderStatus:
    CREATED = "created"
    PAID = "paid"
    FAILED = "failed"
    CANCELLED = "cancelled"


class OrderBase(BaseModel):
    amount: int = Field(..., gt=0, example=50000, description="Amount in smallest unit (e.g. paise)")
    currency: str = Field("INR", example="INR")
    receipt: Optional[str] = Field(None, example="rcpt_11")
    user_id: Optional[str] = Field(None, example="user_123")


class OrderCreate(OrderBase):
    pass


class OrderInDB(OrderBase):
    id: str = Field(..., alias="_id")
    status: str = Field(default=OrderStatus.CREATED)
    created_at: datetime

    class Config:
        allow_population_by_field_name = True


class OrderPublic(OrderBase):
    id: str
    status: str
    created_at: datetime


