from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from app.models.TodoModal import TodoModal, TodoUpdate
from app.response.todo import TodoResponse, TodoCreateResponse
from app.database.mysql import get_db
from sqlalchemy.orm import Session
from app.controllers.TodoController import (
    create_todo,
    get_todos,
    get_todo,
    update_todo,
    delete_todo,
)
from app.middleware.jwt_verify import authenticate_user

router = APIRouter(prefix="/todo",dependencies=[Depends(authenticate_user)])

@router.get("/", response_model=List[TodoResponse])
def get_todo_list(db: Session = Depends(get_db)):
    todos = get_todos(db)
    return todos


@router.post("/created", response_model=TodoCreateResponse)
def created(todo: TodoModal, db: Session = Depends(get_db)):
    create = create_todo(db, todo)
    return {"message": "Todo created successfully", "todo": create}


@router.get("/{id}", response_model=TodoResponse)
def index(id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{id}")
def updated(id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated = update_todo(db, id, todo)

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated


@router.delete("/{id}")
def deleted(id: int, db: Session = Depends(get_db)):
    deleted = delete_todo(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted successfully"}
