from datetime import date

from app.repository.base import BaseDAO
from app.database import async_session_maker
from app.projects.models import Projects


class ProjectDAO(BaseDAO):
    model = Projects
