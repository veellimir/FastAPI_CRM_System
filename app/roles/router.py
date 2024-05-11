from typing import List

from fastapi import APIRouter, Depends

from app.roles.dao import RoleDAO
from app.roles.schemes import SGetRole
from app.users.models import Users

from app.users.dependecies import current_user

from app.exeptions import RoleAlreadyExistsException


router = APIRouter(
    prefix="/roles",
    tags=["Роль пользователей"]
)


@router.post(
    "/create",
    summary="создать роль",
)
async def create_role(name: str, users: Users = Depends(current_user)):
    existing_role = await RoleDAO.find_one_by_name(name)
    if existing_role:
        raise RoleAlreadyExistsException

    role = await RoleDAO.add(name)
    return f"Роль: {name} создана"


@router.delete(
    "/delete{role_id}",
    summary="удалить роль"
)
async def delete_role(
        role_id: int,
        users: Users = Depends(current_user)
):
    role = await RoleDAO.delete(role_id)
    return "Роль удалена"


@router.get(
    "/all",
    summary="получить список ролей",
    response_model=List[SGetRole]
)
async def get_all_roles(user: Users = Depends(current_user)):
    roles = await RoleDAO.find_all()
    roles.sort(key=lambda role: role.id)
    return roles
