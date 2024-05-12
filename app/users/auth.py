from datetime import timedelta, datetime

from jose import jwt
from asyncpg.pgproto.pgproto import timedelta
from passlib.context import CryptContext

from pydantic import EmailStr

from app.users.dao import UsersDAO
from app.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hashed(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})

    encode_jwt = jwt.encode(
        to_encode, SECRET_KEY, ALGORITHM
    )
    return encode_jwt


async def authenticated_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none_users(email=email)

    if user and verify_password(password, user.hashed_password):
        return user
    else:
        return None
