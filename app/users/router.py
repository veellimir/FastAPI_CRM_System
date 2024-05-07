from fastapi import APIRouter, Depends

from app.users.models import Users, Roles

router = APIRouter(
    prefix='/Пользователи',
    tags=['Пользователей']
)

