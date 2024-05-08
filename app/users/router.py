from typing import List

from fastapi import APIRouter, Response, Depends

from users.schemes import SUserAuth, SGetUser
from users.dao import UsersDAO
from users.auth import get_password_hashed, authenticated_user, create_access_token
from users.models import Users
from users.dependecies import current_user
from exeptions import UserAlreadyExistsException, IncorrectEmailOrPswException

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.post("/регистрация")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hashed(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    return f"Пользователь {user_data.email} успешно зарегистрирован"


@router.post("/войти")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticated_user(user_data.email, user_data.password)

    if not user:
        raise IncorrectEmailOrPswException

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("crm_system_access_token", access_token, httponly=True)
    return f"Вы {user.email} вошли в систему"


@router.post("/выйти")
async def logout_user(response: Response):
    response.delete_cookie('crm_system_access_token')
    return "Вы вышли"


@router.get("/получить текущего пользователя")
async def get_current_user(user: Users = Depends(current_user)):
    return SGetUser(id=user.id, email=user.email)


@router.get("/получить всех пользователей", response_model=List[SGetUser])
async def get_all_users():
    users = await UsersDAO.find_all()
    return [SGetUser(id=user.id, email=user.email) for user in users]