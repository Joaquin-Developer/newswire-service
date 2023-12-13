from pydantic import BaseModel


class Newswire(BaseModel):
    id: int
    title: str
    text: str
    created_at: str
    notify_on_insert: bool
