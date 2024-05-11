from typing import List

from fastapi import APIRouter, Depends

from app.users.schemes import SGetUser
from app.users.dao import UsersDAO
from app.users.models import Users


from app.users.dependecies import current_user


router = APIRouter(
    prefix="/users_data",
    tags=["Пользователи"]
)


@router.get(
    "/get_all_users",
    summary="получить список пользователей",
    response_model=List[SGetUser]
)
async def get_all_users(users: Users = Depends(current_user)):
    users = await UsersDAO.find_all()
    return [SGetUser(id=user.id, role_id=user.role_id, email=user.email) for user in users]


@router.get(
    "/get_current_user",
    summary="получить текущего пользователя"
)
async def get_current_user(user: Users = Depends(current_user)):
    return SGetUser(id=user.id, role_id=user.role_id, email=user.email)