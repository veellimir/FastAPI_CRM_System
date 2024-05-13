from app.repository.base import BaseDAO
from app.database import async_session_maker

from app.finance.models import Finance, Profit


class FinanceDAO(BaseDAO):
    model = Finance


class ProfitDAO(BaseDAO):
    model = Profit
