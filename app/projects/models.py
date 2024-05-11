from sqlalchemy import Column, String, Integer, Date, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    date_create = Column(Date, default=func.now())

    tasks = relationship("Tasks", back_populates="projects")

    users = relationship(
        "ProjectUserAssociation",
        back_populates="projects"
    )


class ProjectUserAssociation(Base):
    __tablename__ = 'project_user_association'

    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    projects = relationship("Projects", back_populates="users")
    users = relationship("Users", back_populates="projects")