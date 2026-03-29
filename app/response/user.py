from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserCreateResponse(BaseModel):
    message: str
    user: UserResponse
