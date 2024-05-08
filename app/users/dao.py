from users.models import Users
from repository.base import BaseDAO


class UsersDAO(BaseDAO):
    model = Users
