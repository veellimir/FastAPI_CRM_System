from sqlalchemy import Column, Integer, String, ForeignKey, Date, func
from sqlalchemy.orm import relationship

from app.database import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    name_task = Column(String(100), nullable=False)
    description = Column(String)
    date_create = Column(Date, default=func.now())
    deadline = Column(Date, nullable=False)
    user = relationship("Users", back_populates="tasks")

    def __str__(self):
        return f"Задачи {self.name_task}"