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


def test__parse_ineco_expense__with_two_cards_right_card():
    card_one, card_two, default_text, default_time, company = default_data()

    message = SmsMessage(default_text, company, default_time)
    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.amount == 1096
    assert expence.card.last_digits == '4511'
    assert expence.card.owner == 'Petrov'


def test__parse_ineco_expense__with_two_cards_right_parse_store():
    card_one, card_two, default_text, default_time, company = default_data()

    message = SmsMessage(default_text, company, default_time)
    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.spent_in == '4lapi'
    assert expence.spent_at == datetime.datetime(2023, 12, 6, 13, 12)


def test__parse_ineco_expense__with_two_cards_right_rarse_datetime():
    card_one, card_two, default_text, default_time, company = default_data()

    message = SmsMessage(default_text, company, default_time)
    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.spent_at == datetime.datetime(2023, 12, 6, 13, 12)


def test__parse_ineco_expense__smsmessage_bad_text_with_wrong_time_format_raise_valuerror():
    card_one, card_two, _, default_time, company = default_data()

    message = SmsMessage('1096 rub, 1234567812234511 06.12.23 13.12 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(ValueError):
        parse_ineco_expense(message, [card_one, card_two])


def test__parse_ineco_expense__smsmessage_bad_text_without_datetime_raise_valueerror():
    card_one, card_two, _, default_time, company = default_data()

    message = SmsMessage('1096 rub, 1234567812234511 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(ValueError):
        parse_ineco_expense(message, [card_one, card_two])


def test__parse_ineco_expense__smsmessage_bad_sms_text_with_sum_format_without_currency_raise_indexerror():
    card_one, card_two, _, default_time, company = default_data()

    message = SmsMessage('1096, 1234567812234511 06.12.23 13.12 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(IndexError):
        parse_ineco_expense(message, [card_one, card_two])
