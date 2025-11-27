from fastapi import APIRouter
from app.controllers.user_controller import create_user, get_all_users

user_router = APIRouter()

@user_router.post("/")
async def register_user(data: dict):
    return await create_user(data)

@user_router.get("/")
async def fetch_users():
    return await get_all_users()
