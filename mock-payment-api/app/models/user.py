from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., example="Razor User")
    email: EmailStr = Field(..., example="user@example.com")
    contact: Optional[str] = Field(None, example="+911234567890")


class UserCreate(UserBase):
    pass


class UserInDB(UserBase):
    id: str = Field(..., alias="_id")
    created_at: datetime

    class Config:
        allow_population_by_field_name = True


class UserPublic(UserBase):
    id: str
    created_at: datetime


