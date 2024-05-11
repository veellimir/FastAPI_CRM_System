# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
#
#
# from app.database import Base


# class ProjectUserAssociation(Base):
#     __tablename__ = 'project_user_association'
#
#     project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#
#     projects = relationship("Projects", back_populates="users")
#     users = relationship("Users", back_populates="projects")


