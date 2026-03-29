from pwdlib import PasswordHash
from app.config.app_config import getAppConfig
from datetime import datetime, timedelta
import jwt

# create instance (argon2 is default & recommended)
password_hash = PasswordHash.recommended()
config = getAppConfig()


def hashPassword(password: str) -> str:
    return password_hash.hash(password)


def verifyPassword(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def createAccessToken(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=config.access_token_expire_minutes)

    to_encode.update({"exp": expire, "type": "access"})

    return jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)


def createRefreshToken(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(days=config.refresh_token_expire_days)

    to_encode.update({"exp": expire, "type": "refresh"})

    return jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)
