from pydantic import BaseModel

class Payment(BaseModel):
    order_id: str
    amount: float
    currency: str
    status: str
    created_at: str
