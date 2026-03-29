from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TodoCreateResponse(BaseModel):
    message: str
    todo: TodoResponse
