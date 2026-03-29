from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class AppConfig(BaseSettings):
    app_name: str
    app_env: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def getAppConfig():
    return AppConfig()  # type: ignore
