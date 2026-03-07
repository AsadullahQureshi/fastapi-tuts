from pydantic import BaseModel, Field
from typing import Optional


class TodoModal(BaseModel):
    content: str = Field(..., min_length=4, max_length=50)
    completed: bool
