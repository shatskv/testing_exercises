import datetime

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage


@pytest.fixture
def default_text():
    return '1096 rub, 1234567812234511 06.12.23 13:12 4lapi authcode 345562'


@pytest.fixture
def default_time():
    return datetime.datetime.now() - datetime.timedelta(hours=1)


@pytest.fixture
def urls():
    return 'google.com', 'account'


@pytest.fixture
def company():
    return 'Tinkoff'


@pytest.fixture
def message(default_text, company, default_time):
    company = 'Tinkoff'
    return  SmsMessage(default_text, company, default_time)


@pytest.fixture
def bank_data():
    card_one = BankCard('4567', 'Petrov')
    card_two = BankCard('4511', 'Petrov')

    return card_one, card_two


@pytest.fixture
def today():
    return datetime.datetime.today()
