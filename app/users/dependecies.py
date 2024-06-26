from datetime import datetime

from fastapi import Request, Depends, Header
from jose import jwt, JWTError

from app.config import SECRET_KEY, ALGORITHM
from app.users.dao import UsersDAO


from app.exeptions import (
    TokenAbsentException,
    IncorrectTokenFormatExeption,
    TokenExpireException,
    UserNotPresentException,
)


# def get_token(request: Request) -> str:
#     token = request.cookies.get("crm_system_access_token")
#
#     if not token:
#         raise TokenAbsentException
#     return token


def get_token(request: Request) -> str:
    authorization: str = request.headers.get("Authorization")
    if authorization:
        try:
            scheme, token = authorization.split()
            if scheme.lower() != "bearer":
                raise IncorrectTokenFormatExeption
            return token
        except ValueError:
            raise IncorrectTokenFormatExeption

    token = request.cookies.get("crm_system_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatExeption

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpireException

    user_id: str = payload.get("sub")
    if not user_id:
        raise UserNotPresentException

    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserNotPresentException
    return user

