import datetime

import pytest

from functions.level_1.four_bank_parser import (BankCard, SmsMessage,
                                                parse_ineco_expense)


def default_data():
    card_one = BankCard('4567', 'Petrov')
    card_two = BankCard('4511', 'Petrov')
    default_text = '1096 rub, 1234567812234511 06.12.23 13:12 4lapi authcode 345562'
    default_time = datetime.datetime.now() - datetime.timedelta(hours=1)
    company = 'Tinkoff'

    return card_one, card_two, default_text, default_time, company


def test__parse_ineco_expense__with_two_cards():
    card_one, card_two, default_text, default_time, company = default_data()

    message = SmsMessage(default_text, company, default_time)
    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.amount == 1096
    assert expence.card.last_digits == '4511'
    assert expence.card.owner == 'Petrov'
    assert expence.spent_in == '4lapi'
    assert expence.spent_at == datetime.datetime(2023, 12, 6, 13, 12)


def test__parse_ineco_expense__change_smsmesage_text_exc_attributeerror():
    _, _, default_text, default_time, company = default_data()

    message = SmsMessage(default_text, company, default_time)

    with pytest.raises(AttributeError):
        message.text = '1096 rub, 1234567812234511 06.12.23 13.12 4lapi authcode 345562'


def test__parse_ineco_expense__smsmessage_bad_time_format_exc_valuerror():
    card_one, card_two, _, default_time, company = default_data()

    message = SmsMessage('1096 rub, 1234567812234511 06.12.23 13.12 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(ValueError):
        parse_ineco_expense(message, [card_one, card_two])


def test__parse_ineco_expense__smsmessage_bad_no_datetime_exc_valueerror():
    card_one, card_two, _, default_time, company = default_data()

    message = SmsMessage('1096 rub, 1234567812234511 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(ValueError):
        parse_ineco_expense(message, [card_one, card_two])


def test__parse_ineco_expense__smsmessage_bad_smsmmesage_sum_format_no_currency_exc_indexerror():
    card_one, card_two, _, default_time, company = default_data()

    message = SmsMessage('1096, 1234567812234511 06.12.23 13.12 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(IndexError):
        parse_ineco_expense(message, [card_one, card_two])
