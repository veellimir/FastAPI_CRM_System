from sqlalchemy import Column, String, Integer, ForeignKey, Date, func
from sqlalchemy.orm import relationship

from app.database import Base


class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    date_create = Column(Date, default=func.now())

    tasks = relationship("Tasks", back_populates="projects")