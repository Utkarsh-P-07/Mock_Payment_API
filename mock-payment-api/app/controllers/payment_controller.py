from app.config.database import payments_collection
from app.schemas.payment_schema import payment_serializer, list_payments
from datetime import datetime
import uuid

async def create_payment(data):
    data["order_id"] = str(uuid.uuid4())
    data["created_at"] = str(datetime.utcnow())
    data["status"] = "created"

    response = payments_collection.insert_one(data)
    return payment_serializer(payments_collection.find_one({"_id": response.inserted_id}))

async def update_payment(order_id: str, new_status: str):
    payments_collection.update_one({"order_id": order_id}, {"$set": {"status": new_status}})
    return payment_serializer(payments_collection.find_one({"order_id": order_id}))

async def get_all_payments():
    return list_payments(payments_collection.find())
