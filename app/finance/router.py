from typing import List

from fastapi import APIRouter, Depends

from app.users.dependecies import current_user

from app.finance.shemes import SGetFinance, SGetProfit
from app.finance.dao import FinanceDAO, ProfitDAO
from app.users.models import Users

router = APIRouter(
    prefix="/finance",
    tags=["Финансы компании"]
)


@router.post(
    "/add_profit",
    summary="добавить прибыль",
)
async def add_profit(
        profit: int,
        name_profit: str,
        description_profit: str = None,
        users: Users = Depends(current_user)
):
    profit_data = {
        "profit": profit,
        "name_profit": name_profit,
        "description_profit": description_profit
    }
    profit_entry = await ProfitDAO.add_kwargs(**profit_data)
    finance = await FinanceDAO.find_all()

    profit_after_tax = int(profit * 0.87)
    finance[0].all_tax += profit - profit_after_tax
    finance[0].current_balance += profit_after_tax

    await FinanceDAO.update(finance[0])
    return profit_data


@router.get(
    "/get_finance",
    summary="получить информацию о финансах",
    response_model=List[SGetFinance]
)
async def get_finance(users: Users = Depends(current_user)):
    finance = await FinanceDAO.find_all()
    return finance


@router.get(
    "/get_profit",
    summary="получить всю прибыль",
    response_model=List[SGetProfit]
)
async def get_profit( users: Users = Depends(current_user)) -> List[SGetProfit]:
    profits = await ProfitDAO.find_all()
    return profits
