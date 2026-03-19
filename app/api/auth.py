from fastapi import APIRouter, Depends, HTTPException
from app.models.User import Register, Login, UserResponse
from app.database.mysql import get_db
from sqlalchemy.orm import Session
from app.controllers.UserController import (register, login)

router = APIRouter(prefix="/auth")


@router.post("/login")
def userLogin(user:Login,db: Session = Depends(get_db)):
    tokens = login(db,user)
    return tokens


@router.post("/register", response_model=UserResponse)
def userRegister(user: Register, db: Session = Depends(get_db)):
    user = register(db, user)
    return {"message": "Todo created successfully", "todo": user}
