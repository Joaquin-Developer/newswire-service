import os

from pydantic import BaseSettings


env = os.getenv("ENV") or "development"
env_dir = os.getenv("ENV_DIR") or os.getcwd()


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    class Config:
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings(_env_file=f"{env_dir}/environments/.env.{env}", ENVIRONMENT=env)
