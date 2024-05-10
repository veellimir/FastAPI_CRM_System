from pydantic import BaseModel, EmailStr

from typing import Optional


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SGetUser(BaseModel):
    id: int
    role_id: Optional[int]
    email: str

