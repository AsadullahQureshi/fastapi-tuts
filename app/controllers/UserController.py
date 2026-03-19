from sqlalchemy.orm import Session
from app.database.schema import UserSchema
from app.models.User import Register, Login

def register(db: Session, user: Register):
    # hashed = hash_password(user.password)
    user = UserSchema(name=user.name, email=user.email,password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db: Session, user:Login):
    db_user = db.query(UserSchema).filter(UserSchema.email == user.email).first()
    
    # check for password match with db password 
    # if not db_user or not verify_password(user.password, db_user.password):
    #     return {"error": "Invalid credentials"}

    # create token
    # token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": "",
        "token_type": "bearer"
    }