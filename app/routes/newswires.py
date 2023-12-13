from fastapi import APIRouter


newswires_router = APIRouter()


@newswires_router.post("/create")
def create_newswire():
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
