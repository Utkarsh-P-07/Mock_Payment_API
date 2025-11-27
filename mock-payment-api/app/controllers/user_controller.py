from app.config.database import users_collection
from app.schemas.user_schema import user_serializer, list_users
from datetime import datetime

async def create_user(data):
    data["created_at"] = str(datetime.utcnow())
    response = users_collection.insert_one(data)
    return user_serializer(users_collection.find_one({"_id": response.inserted_id}))

async def get_all_users():
    return list_users(users_collection.find())
