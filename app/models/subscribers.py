from pydantic import BaseModel


class Subscribers(BaseModel):
    id: int
    mail: str
