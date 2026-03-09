from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.app_config import getAppConfig
from urllib.parse import quote_plus

config = getAppConfig()
password = quote_plus(config.db_password)

DATABASE_URL = f"mysql+pymysql://{config.db_user}:{password}@{config.db_host}:{config.db_port}/{config.db_name}"

print(DATABASE_URL)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
