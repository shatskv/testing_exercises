from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from decimal import Decimal
from datetime import timedelta

def test__calculate_average_daily_expenses__three_expenses_one_day(generate_expense, card, spent_in, datetime_now):
    expenses = []
    for amount in [Decimal(20.50), Decimal(30.50), Decimal(40.50)]:
        expenses.append(generate_expense(amount, card, spent_in, datetime_now))

    assert calculate_average_daily_expenses(expenses) == 91.5


def test__calculate_average_daily_expenses__three_cards_different_days(generate_expense, card, spent_in, datetime_now):
    expenses = []
    amount_and_dates = [
        {'amount': Decimal(20.25), 'days': 0},
        {'amount': Decimal(50.75), 'days': 0},
        {'amount': Decimal(120.15), 'days': 1},
        {'amount': Decimal(220.75), 'days': 1},
        {'amount': Decimal(400.10), 'days': 1},
        {'amount': Decimal(550.50), 'days': 2},
        {'amount': Decimal(675.50), 'days': 2},
    ]
    for record in amount_and_dates:
        expenses.append(generate_expense(record['amount'], card, spent_in, 
                                         datetime_now - timedelta(days=record['days'])))
    
    assert round(calculate_average_daily_expenses(expenses), 5) == round(Decimal(679.33333), 5)
