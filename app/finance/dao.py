from app.repository.base import BaseDAO
from app.database import async_session_maker

from app.finance.models import Finance, Profit


class FinanceDAO(BaseDAO):
    model = Finance

    @staticmethod
    async def update(finance: Finance):
        async with async_session_maker() as session:
            async with session.begin():
                await session.merge(finance)
                await session.commit()


class ProfitDAO(BaseDAO):
    model = Profit