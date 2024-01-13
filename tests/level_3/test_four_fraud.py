from datetime import timedelta
from decimal import Decimal

import pytest

from functions.level_3.four_fraud import find_fraud_expenses


@pytest.mark.parametrize(
        'expenses_data,fraud_transactions_data', [
        (
            [
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 2},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 1}
            ],
            [
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
            ]
        ),

        (
            [
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 2},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 1},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
            ],
            [
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
            ]
        )
    ]
)
def test__find_fraud_expenses__fraud_transactions_not_emmpty(generate_expense, card, expenses_data, fraud_transactions_data, datetime_now, get_datatime_months_ago):
    expenses = []
    fraud_transactions = []
    for record in expenses_data:
        expenses.append(generate_expense(record['amount'], card, record['spent_in'],
                                         get_datatime_months_ago(datetime_now, record['days'])))

    for record in fraud_transactions_data:
        fraud_transactions.append(generate_expense(record['amount'], card, record['spent_in'], 
                                                   get_datatime_months_ago(datetime_now, record['days'])))
    assert find_fraud_expenses(expenses) == fraud_transactions


@pytest.mark.parametrize(
        'expenses_data,fraud_transactions_data', [
        (
            [
                {'amount': Decimal(6000), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 2},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 1}
            ],
            []
        ),

        (
            [
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 2},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
                {'amount': Decimal(400), 'spent_in': 'netflix', 'days': 1},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 0},
                {'amount': Decimal(300), 'spent_in': 'apple', 'days': 1},
            ],
            []
        )
    ]
)
def test__find_fraud_expenses__fraud_transactions_not_emmpty(generate_expense, card, expenses_data, fraud_transactions_data, datetime_now, get_datatime_months_ago):
    expenses = []
    fraud_transactions = []
    for record in expenses_data:
        expenses.append(generate_expense(record['amount'], card, record['spent_in'],
                                         get_datatime_months_ago(datetime_now, record['days'])))

    for record in fraud_transactions_data:
        fraud_transactions.append(generate_expense(record['amount'], card, record['spent_in'], 
                                                   get_datatime_months_ago(datetime_now, record['days'])))
    assert find_fraud_expenses(expenses) == fraud_transactions
