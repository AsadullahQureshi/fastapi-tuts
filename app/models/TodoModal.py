from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TodoModal(BaseModel):
    title: str = Field(..., min_length=4, max_length=50)
    completed: bool


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=4, max_length=50)
    completed: Optional[bool] = None


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