from fastapi import APIRouter, Response

from app.users.schemes import SUserReg, SUserLogin
from app.users.dao import UsersDAO

from app.users.auth import get_password_hashed, authenticated_user, create_access_token

from app.exeptions import UserAlreadyExistsException, IncorrectEmailOrPswException


router = APIRouter(
    prefix="/users",
    tags=["Аутентификация"]
)


@router.post(
    "/register_user",
    summary="регистрация пользователя"
)
async def register_user(response: Response, user_data: SUserReg):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    existing_user_by_username = await UsersDAO.find_one_or_none(username=user_data.username)

    if existing_user or existing_user_by_username:
        raise UserAlreadyExistsException

    hashed_password = get_password_hashed(user_data.password)
    await UsersDAO.add(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password
    )

    # access_token = await login_user_and_set_cookie(
    #     response, user_data.email, user_data.password
    # )
    return f"Пользователь {user_data.username} зарегистрирован"


@router.post("/login", summary="войти")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticated_user(user_data.email, user_data.password)

    if not user:
        raise IncorrectEmailOrPswException

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("crm_system_access_token", access_token, httponly=True, secure=True)
    return access_token


@router.post("/logout", summary="выйти")
async def logout_user(response: Response):
    response.delete_cookie('crm_system_access_token')
    return "Вы вышли"
