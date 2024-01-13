from datetime import datetime, timedelta
from decimal import Decimal
from typing import Callable

import pytest

from functions.level_3.models import BankCard, Currency, Expense


@pytest.fixture
def card() -> BankCard:
    return BankCard(last_digits='1234', owner='Vladimir')


@pytest.fixture
def spent_in() -> str:
    return '4lapi'


@pytest.fixture
def datetime_now() -> datetime:
    return datetime.now()


@pytest.fixture
def amount() -> Decimal:
    return Decimal(150.0)


@pytest.fixture
def generate_expense() -> Callable[[Decimal, BankCard, str, datetime], Expense]:
    def _generate_expense(amount, card, spent_in, spent_at):
        expense = Expense(amount=amount, currency=Currency.RUB, card=card, spent_in=spent_in,
                          spent_at=spent_at , category=None)
        return expense
    return _generate_expense


@pytest.fixture
def expenses_data_subscription(spent_in: str, datetime_now: datetime, 
                               get_datatime_months_ago: Callable[[datetime, int], datetime]) -> dict[str, str | datetime]:
    data = [
        {'spent_in': spent_in, 'spent_at': datetime_now},
        {'spent_in': 'netflix', 'spent_at': datetime_now - timedelta(days=1)},
        {'spent_in': spent_in, 'spent_at': get_datatime_months_ago(datetime_now, 1)},
        {'spent_in': 'netflix', 'spent_at': get_datatime_months_ago(datetime_now, 1)},
        {'spent_in': spent_in, 'spent_at': get_datatime_months_ago(datetime_now, 2)},
        {'spent_in': 'netflix', 'spent_at': get_datatime_months_ago(datetime_now, 2)}, 
    ]
    return data


@pytest.fixture
def get_datatime_months_ago() -> Callable[[datetime, int], datetime]:
    def _get_datatime_months_ago(datetime_, month_ago):
        day = datetime_.day
        month = datetime_.month
        year = datetime_.year
        month = month - month_ago % 12
        if month < 1:
            month += 12
            year -= 1
        year = year - month_ago // 12
        return datetime(year, month, day, datetime_.hour, datetime_.minute)
    return _get_datatime_months_ago
