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
    "/all",
    summary="получить список пользователей",
    response_model=List[SGetUser]
)
async def get_all_users(users: Users = Depends(current_user)):
    users = await UsersDAO.find_all()
    return [
        SGetUser(
            id=user.id,
            role_id=user.role_id,
            email=user.email,
            username=user.username
        ) for user in users]


@router.get(
    "/current{user_id}",
    summary="получить текущего пользователя",
)
async def get_current_user(user_id: int, users: Users = Depends(current_user)):
    user = await UsersDAO.find_by_id(model_id=user_id)
    return SGetUser(
        id=user.id,
        role_id=user.role_id,
        email=user.email,
        username=user.username
    )
