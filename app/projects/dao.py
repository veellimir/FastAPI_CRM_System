from datetime import date

from sqlalchemy import select, insert

from app.database import async_session_maker
from app.repository.base import BaseDAO

from app.projects.models import Projects, ProjectUserAssociation


class ProjectDAO(BaseDAO):
    model = Projects

    @classmethod
    async def add_project(cls, name: str, description: str, date_create: date):
        async with async_session_maker() as session:
            new_project = (
                insert(Projects).values(
                    name=name,
                    description=description,
                    date_create=date_create,
                ).returning(Projects)
            )
            add_new_project = await session.execute(new_project)
            await session.commit()
            return add_new_project.scalars()


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