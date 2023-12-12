from fastapi import FastAPI

from app.core.config import settings
from app.routes.subscriptions import subscriptions_router


app = FastAPI(settings.APP_NAME)


app.include_router(subscriptions_router, prefix="")
