from sqlalchemy.orm import Session
from app.database.schema import UserSchema
from app.models.User import Register, Login
from app.core.security.jwt_helper import (
    hashPassword,
    verifyPassword,
    createAccessToken,
    createRefreshToken,
)


def register(db: Session, user: Register):
    hashed = hashPassword(user.password)

    user = UserSchema(name=user.name, email=user.email, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login(db: Session, user: Login):
    db_user = db.query(UserSchema).filter(UserSchema.email == user.email).first()

    # check for password match with db password
    if not db_user or not verifyPassword(user.password, db_user.password):
        return {"error": "Invalid credentials"}

    # create token
    access_token = createAccessToken({"user_id": db_user.id, "email": db_user.email})
    refresh_token = createRefreshToken({"user_id": db_user.id})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
