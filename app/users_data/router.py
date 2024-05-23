from typing import List

from fastapi import APIRouter, Depends, UploadFile, File

from app.users.schemes import SGetUser
from app.users.dao import UsersDAO
from app.users.models import Users

from app.users.dependecies import current_user

from app.exeptions import IncorrectTokenFormatExeption


router = APIRouter(
    prefix="/users_data",
    tags=["Пользователи"]
)


@router.post(
    "/profile_image",
    summary="загрузить изображения пользователя"
)
async def load_profile_image(
        user_id: int,
        image: UploadFile = File(...),
        users: Users = Depends(current_user)
):
    filename = f"app/static/profile_img_users_{user_id}_{image.filename}"
    with open(filename, "wb") as file:
        file.write(image.file.read())

    user = await UsersDAO.upload_user_image(user_id, filename)
    if not user:
        raise IncorrectTokenFormatExeption

    return {f"Изображения: {filename} загружено"}


@router.delete(
    "/delete_image",
    summary="удалить изображения пользователя"
)
async def delete_profile_image(
        user_id: int, users: Users = Depends(current_user)
):
    user = await UsersDAO.find_by_id(user_id)

    if not user:
        raise IncorrectTokenFormatExeption

    user.user_image = None
    await UsersDAO.update(user)
    return "Изображения удалено"


@router.post(
    "/all",
    summary="получить список пользователей",
    response_model=List[SGetUser]
)
async def get_all_users(user: Users = Depends(current_user)):
    users = await UsersDAO.find_all()
    return [
        SGetUser(
            id=user.id,
            role_id=user.role_id,
            email=user.email,
            username=user.username,
            user_image=user.user_image
        ) for user in users]


@router.post(
    "/current",
    summary="получить текущего пользователя",
)
async def get_current_user(user: Users = Depends(current_user)):
    return SGetUser(
        id=user.id,
        role_id=user.role_id,
        email=user.email,
        username=user.username,
        user_image=user.user_image
    )
