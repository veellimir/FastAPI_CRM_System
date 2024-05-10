from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SGetUser(BaseModel):
    id: int
    role_id: int
    email: str

