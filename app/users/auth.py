from datetime import timedelta, datetime

from jose import jwt
from asyncpg.pgproto.pgproto import timedelta
from passlib.context import CryptContext

from pydantic import EmailStr

from app.users.dao import UsersDAO
from app.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hashed(psw: str) -> str:
    return pwd_context.hash(psw)


def verify_password(plain_psw, hashed_psw) -> bool:
    return pwd_context.verify(plain_psw, hashed_psw)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(
        to_encode, SECRET_KEY, ALGORITHM
    )
    return encode_jwt


async def authenticated_user(email: EmailStr, psw: str):
    user = await UsersDAO.find_one_or_none(email=email)

    if not user and verify_password(psw, user.password):
        return None
    return user
