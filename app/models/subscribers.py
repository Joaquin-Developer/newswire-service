from pydantic import BaseModel, Field


class Subscribers(BaseModel):
    id: int = Field(default=None, alias="_id")
    mail: str
    active: bool
