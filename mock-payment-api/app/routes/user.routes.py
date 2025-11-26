from fastapi import APIRouter, HTTPException, status

from ..models.user import UserCreate, UserPublic
from ..services import create_user, get_user

router = APIRouter()


@router.post("", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(payload: UserCreate):
    user = await create_user(payload)
    return UserPublic(**user.dict(by_alias=False))


@router.get("/{user_id}", response_model=UserPublic)
async def get_user_endpoint(user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserPublic(**user.dict(by_alias=False))


