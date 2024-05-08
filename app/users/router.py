from typing import List

from fastapi import APIRouter, Response, Depends

from app.users.schemes import SUserAuth, SGetUser
from app.users.dao import UsersDAO
from app.users.auth import get_password_hashed, authenticated_user, create_access_token
from app.users.models import Users
from app.users.dependecies import current_user
from app.exeptions import UserAlreadyExistsException, IncorrectEmailOrPswException

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.post(
    "/register_user",
    summary="регистрация пользователя"
)
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hashed(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    return f"Пользователь {user_data.email} успешно зарегистрирован"


@router.post("/login", summary="войти")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticated_user(user_data.email, user_data.password)

    if not user:
        raise IncorrectEmailOrPswException

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("crm_system_access_token", access_token, httponly=True)
    return f"Вы {user.email} вошли в систему"


@router.post("/logout", summary="выйти")
async def logout_user(response: Response):
    response.delete_cookie('crm_system_access_token')
    return "Вы вышли"


@router.get(
    "/get_all_users",
    summary="получить список пользователей",
    response_model=List[SGetUser]
)
async def get_all_users(users: Users = Depends(current_user)):
    users = await UsersDAO.find_all()
    return [SGetUser(id=user.id, email=user.email) for user in users]


@router.get(
    "/get_current_user",
    summary="получить текущего пользователя"
)
async def get_current_user(user: Users = Depends(current_user)):
    return SGetUser(id=user.id, email=user.email)