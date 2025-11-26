from datetime import datetime
from typing import Any, Dict, List, Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from .config import get_settings
from .models.order import OrderCreate, OrderInDB, OrderStatus
from .models.payment import PaymentCaptureRequest, PaymentInDB, PaymentStatus
from .models.user import UserCreate, UserInDB


settings = get_settings()

_mongo_client: Optional[AsyncIOMotorClient] = None


def get_mongo_client() -> AsyncIOMotorClient:
    global _mongo_client
    if _mongo_client is None:
        _mongo_client = AsyncIOMotorClient(settings.mongo_uri)
    return _mongo_client


def get_db() -> AsyncIOMotorDatabase:
    client = get_mongo_client()
    return client[settings.mongo_db_name]


def _object_id() -> str:
    return str(ObjectId())


def _to_public(doc: Dict[str, Any]) -> Dict[str, Any]:
    if not doc:
        return doc
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc


# User services
async def create_user(data: UserCreate) -> UserInDB:
    db = get_db()
    now = datetime.utcnow()
    doc = {
        "_id": _object_id(),
        "name": data.name,
        "email": data.email,
        "contact": data.contact,
        "created_at": now,
    }
    await db.users.insert_one(doc)
    return UserInDB(**_to_public(doc))


async def get_user(user_id: str) -> Optional[UserInDB]:
    db = get_db()
    doc = await db.users.find_one({"_id": user_id})
    if not doc:
        return None
    return UserInDB(**_to_public(doc))


# Order services
async def create_order(data: OrderCreate) -> OrderInDB:
    db = get_db()
    now = datetime.utcnow()
    doc = {
        "_id": _object_id(),
        "amount": data.amount,
        "currency": data.currency,
        "receipt": data.receipt,
        "user_id": data.user_id,
        "status": OrderStatus.CREATED,
        "created_at": now,
    }
    await db.orders.insert_one(doc)
    return OrderInDB(**_to_public(doc))


async def get_order(order_id: str) -> Optional[OrderInDB]:
    db = get_db()
    doc = await db.orders.find_one({"_id": order_id})
    if not doc:
        return None
    return OrderInDB(**_to_public(doc))


async def list_orders(limit: int = 20) -> List[OrderInDB]:
    db = get_db()
    cursor = db.orders.find().sort("created_at", -1).limit(limit)
    orders: List[OrderInDB] = []
    async for doc in cursor:
        orders.append(OrderInDB(**_to_public(doc)))
    return orders


async def mark_order_paid(order_id: str) -> None:
    db = get_db()
    await db.orders.update_one(
        {"_id": order_id},
        {"$set": {"status": OrderStatus.PAID}},
    )


# Payment services
async def capture_payment(data: PaymentCaptureRequest) -> Optional[PaymentInDB]:
    db = get_db()

    # Ensure order exists
    order_doc = await db.orders.find_one({"_id": data.order_id})
    if not order_doc:
        return None

    now = datetime.utcnow()
    payment_doc = {
        "_id": _object_id(),
        "order_id": data.order_id,
        "amount": data.amount,
        "currency": data.currency,
        "method": "mock",
        "status": PaymentStatus.CAPTURED,
        "captured": True,
        "created_at": now,
    }
    await db.payments.insert_one(payment_doc)

    await mark_order_paid(data.order_id)

    return PaymentInDB(**_to_public(payment_doc))


async def list_payments(limit: int = 20) -> List[PaymentInDB]:
    db = get_db()
    cursor = db.payments.find().sort("created_at", -1).limit(limit)
    payments: List[PaymentInDB] = []
    async for doc in cursor:
        payments.append(PaymentInDB(**_to_public(doc)))
    return payments


