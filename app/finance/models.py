from sqlalchemy import Column, Integer

from app.database import Base


class Finance(Base):
    __tablename__ = "finance"

    total_amount = Column(Integer)
    profit = Column(Integer)
    losses = Column(Integer)
    tax_report = Column(Integer)
    penalties = Column(Integer)
