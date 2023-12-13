from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes.subscriptions import subscriptions_router
from app.routes.newswires import newswires_router


app = FastAPI(title=settings.APP_NAME)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(subscriptions_router, prefix=settings.API_V1_STR + "/subscriptions")
app.include_router(newswires_router, prefix=settings.API_V1_STR + "/newswires")
