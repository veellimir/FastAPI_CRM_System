from pydantic import BaseModel, EmailStr

from typing import Optional


class SUserReg(BaseModel):
    email: EmailStr
    username: str
    password: str


class SUserLogin(BaseModel):
    email: EmailStr
    password: str


class SGetUser(BaseModel):
    id: int
    role_id: Optional[int]
    email: str
    username: str
