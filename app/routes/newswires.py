from fastapi import APIRouter, BackgroundTasks

from app.models.newswire import Newswire


newswires_router = APIRouter()


@newswires_router.post("/create")
async def create_newswire(new: Newswire, background_tasks: BackgroundTasks):
    # Logica para crear (insertar en MongoDB)

    if new.notify_on_insert:
        # mandar mails en segundo plano

        def background_task():
            print("Hi")

        background_tasks.add_task(background_task, "notify_mails")
        return {"message": "OK. Sending mails..."}

    return {"message": "ok"}


@newswires_router.delete("/delete")
def delete_newswire():
    return {"message": "ok"}


@newswires_router.post("/update")
def update_newswire():
    return {"message": "ok"}


@newswires_router.get("/get_all")
def get_all_newswires():
    return {"message": "ok"}


@newswires_router.get("/get/{newswire_id}")
def get_by_id(newswire_id: str):
    return {"id": newswire_id}
