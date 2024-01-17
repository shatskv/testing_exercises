import datetime

import pytest

from functions.level_1.four_bank_parser import SmsMessage, parse_ineco_expense


def test__parse_ineco_expense__with_two_cards_right_card(bank_data, message):
    card_one, card_two = bank_data

    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.amount == 1096
    assert expence.card.last_digits == '4511'
    assert expence.card.owner == 'Petrov'


def test__parse_ineco_expense__right_expense_amount(bank_data, message):
    card_one, card_two = bank_data

    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.amount == 1096


def test__parse_ineco_expense__with_two_cards_right_parse_store(bank_data, message):
    card_one, card_two = bank_data

    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.spent_in == '4lapi'


def test__parse_ineco_expense__with_two_cards_right_parse_datetime(bank_data, message):
    card_one, card_two = bank_data
    expence = parse_ineco_expense(message, [card_one, card_two])

    assert expence.spent_at == datetime.datetime(2023, 12, 6, 13, 12)


def test__parse_ineco_expense__smsmessage_bad_text_with_wrong_time_format_raise_valuerror(bank_data, default_time, company):
    card_one, card_two = bank_data

    message = SmsMessage('1096 rub, 1234567812234511 06.12.23 13.12 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(ValueError):
        parse_ineco_expense(message, [card_one, card_two])


def test__parse_ineco_expense__smsmessage_bad_text_without_datetime_raise_valueerror(bank_data, default_time, company):
    card_one, card_two = bank_data

    message = SmsMessage('1096 rub, 1234567812234511 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(ValueError):
        parse_ineco_expense(message, [card_one, card_two])


def test__parse_ineco_expense__smsmessage_bad_sms_text_with_sum_format_without_currency_raise_indexerror(bank_data, default_time, company):
    card_one, card_two = bank_data

    message = SmsMessage('1096, 1234567812234511 06.12.23 13.12 4lapi authcode 345562',
                             company, default_time)
    
    with pytest.raises(IndexError):
        parse_ineco_expense(message, [card_one, card_two])
