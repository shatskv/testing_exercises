import datetime

from functions.level_1.four_bank_parser import (BankCard, Expense, SmsMessage,
                                                parse_ineco_expense)
import pytest

def test_parse_ineco_expense():
    card_one = BankCard('4567', 'Petrov')
    card_two = BankCard('4511', 'Petrov')
    default_text = '1096 45, 1234567812234511 06.12.23 13:12 4lapi authcode 345562'
    default_time = datetime.datetime.now() - datetime.timedelta(hours=1)
    company = 'Tinkoff'
    message = SmsMessage(default_text, company, default_time)

    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.amount == 1096
    assert expence.card.last_digits == '4511'
    assert expence.card.owner == 'Petrov'
    assert expence.spent_in == '4lapi'
    assert expence.spent_at == datetime.datetime(2023, 12, 6, 13, 12)
    with pytest.raises(AttributeError):
        message.text = '1096 45, 1234567812234511 06.12.23 13.12 4lapi authcode 345562'
    with pytest.raises(ValueError):
        message = SmsMessage('1096 45, 1234567812234511 06.12.23 13.12 4lapi authcode 345562',
                             company, default_time)
        parse_ineco_expense(message, [card_one, card_two])
    with pytest.raises(ValueError):
        message = SmsMessage('1096 45, 122323 4lapi authcode 345562',
                             company, default_time)
        parse_ineco_expense(message, [card_one, card_two])
    with pytest.raises(IndexError):
        message = SmsMessage('1096, 1234567812234511 06.12.23 13:12 4lapi authcode 345562',
                             company, default_time)
        parse_ineco_expense(message, [card_one, card_two])
    