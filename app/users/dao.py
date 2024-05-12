from app.users.models import Users

from app.repository.base import BaseDAO


class UsersDAO(BaseDAO):
    model = Users

