from sqlalchemy import Integer, String, DateTime
from app.database.mysql import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class UserSchema(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False, index=True)
    email: Mapped[str]= mapped_column(String(100), unique=True, index=True)
    email_verified: Mapped[datetime]= mapped_column(DateTime, nullable=True)
    password: Mapped[str]= mapped_column(String(100),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
