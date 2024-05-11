from sqlalchemy import select

from app.database import async_session_maker
from app.repository.base import BaseDAO

from app.projects.models import Projects, ProjectUserAssociation


class ProjectDAO(BaseDAO):
    model = Projects


class ProjectUserDAO(BaseDAO):
    model = ProjectUserAssociation

    @classmethod
    async def find_projects_by_user_id(cls, user_id):
        async with async_session_maker() as session:
            query = (
                select(Projects)
                .join(ProjectUserAssociation)
                .filter(ProjectUserAssociation.user_id == user_id)
            )
            result = await session.execute(query)
            return result.scalars().all()