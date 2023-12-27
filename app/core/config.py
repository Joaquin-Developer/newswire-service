import os
from typing import List

from pydantic import BaseSettings, AnyHttpUrl


env = os.getenv("ENV") or "development"
env_dir = os.getenv("ENV_DIR") or os.getcwd()


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_V1_STR: str = "/api/v1"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    MONGODB_URL: str
    MONGODB_NAME: str

    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    SMTP_SERVER: str
    SMTP_PORT: int

    class Config:
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings(_env_file=f"{env_dir}/environments/.env.{env}", ENVIRONMENT=env)
