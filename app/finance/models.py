from sqlalchemy import Integer, String, Column

from app.database import Base


class Finance(Base):
    __tablename__ = "finance"

    id = Column(Integer, primary_key=True, nullable=False)
    current_balance = Column(Integer)
    all_tax = Column(Integer)


class Profit(Base):
    __tablename__ = "profit"

    id = Column(Integer, primary_key=True, nullable=False)
    profit = Column(Integer, nullable=False)
    name_profit = Column(String, nullable=False)
    description_profit = Column(String)

