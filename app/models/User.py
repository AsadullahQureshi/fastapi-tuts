from pydantic import BaseModel, Field, EmailStr, ValidationInfo, field_validator
from typing import Optional
from datetime import datetime


class Login(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class Register(BaseModel):
    name: str = Field(..., min_length=4, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    password_confirm: str = Field(..., min_length=8, max_length=128)

    @field_validator("password_confirm")
    @classmethod
    def password_match(cls, v, info: ValidationInfo):
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("Password does not match")
        return v


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
