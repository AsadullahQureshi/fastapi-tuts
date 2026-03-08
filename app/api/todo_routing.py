from fastapi import APIRouter
from typing import Annotated
from app.models.TodoModal import TodoModal


router = APIRouter(prefix="/todo")

@router.get('/')
def index ():
    return {"message": "todo list"}

@router.post("/created")
def created(item:TodoModal):
    return {"message": "Todo Created", "item":item}

@router.put("/todo/{id}")
def updated(id:int):
    return {"message": "Todo Updated", "item":id}

@router.delete("/todo/{id}")
def deleted(id:int):
    return {"message": "Todo deleted", "item":id}
