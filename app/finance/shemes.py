from typing import Optional

from pydantic import BaseModel


class SGetFinance(BaseModel):
    id: int
    current_balance: int
    all_tax: int


class SGetProfit(BaseModel):
    id: int
    profit: int
    name_profit: str
    description_profit: Optional[str]
