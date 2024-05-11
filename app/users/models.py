from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.projects.models import Projects

from app.database import Base


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    user = relationship('Users', back_populates='role')

    def __str__(self):
        return f"Роль {self.name}"


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    user_image = Column(String)
    role_id = Column(Integer, ForeignKey(Roles.id))

    role = relationship("Roles", back_populates="user")
    tasks = relationship("Tasks", back_populates='user')

    projects = relationship(
        "ProjectUserAssociation",
        back_populates="users"
    )

    def __str__(self):
        return f"Пользователь {self.email}"
