from fastapi import APIRouter, Depends, HTTPException
from app.models.User import Register, Login
from app.response.user import UserCreateResponse
from app.database.mysql import get_db
from sqlalchemy.orm import Session
from app.controllers.UserController import register, login
from app.database.schema import UserSchema

router = APIRouter(prefix="/auth")


@router.post("/login")
def userLogin(user: Login, db: Session = Depends(get_db)):
    tokens = login(db, user)
    print(f'asad')
    return tokens


@router.post("/register", response_model=UserCreateResponse)
def userRegister(user: Register, db: Session = Depends(get_db)):
    db_user = db.query(UserSchema).filter(UserSchema.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User with email already existed")
    user = register(db, user)
    return {"message": "user created successfully", "user": user}
