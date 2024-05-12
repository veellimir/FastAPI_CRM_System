from sqlalchemy import select

from app.users.models import Users

from app.repository.base import BaseDAO
from app.database import async_session_maker


class UsersDAO(BaseDAO):
    model = Users

