from pydantic import BaseModel


class SGetRole(BaseModel):
    id: int
    name: str
