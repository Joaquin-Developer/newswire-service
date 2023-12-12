from fastapi import APIRouter


subscriptions_router = APIRouter()


subscriptions_router.get("/subscribe")
def subscribe():
    return {"message": "ok"}
