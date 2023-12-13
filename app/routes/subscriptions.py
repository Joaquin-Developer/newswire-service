from fastapi import APIRouter


from app.models.subscribers import Subscribers
from app.db.mongodb import db


subscriptions_router = APIRouter()


@subscriptions_router.put("/subscribe")
async def subscribe(subscriber: Subscribers):
    subscriber_dict = subscriber.model_dict()
    result = await db.subscribers.insert_one(subscriber_dict)
    return {"subscriber_id": str(result.inserted_id)}


@subscriptions_router.get("/unsubscribe/{mail}")
async def unsubscribe(mail: str):
    result = await db.subscribers.update_one(
        {"mail": mail}, {"$set": {"active": False}}
    )

    if result.modified_count == 1:
        return {"message": f"{mail} deactived!"}
    return {"message": f"{mail} not found"}
