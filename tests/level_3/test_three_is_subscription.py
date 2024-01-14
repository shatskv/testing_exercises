from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__success(generate_expense, amount, card, expenses_data_subscription):
    expenses = []
    for record in expenses_data_subscription:
        expenses.append(generate_expense(amount, card, record['spent_in'], record['spent_at']))

    assert is_subscription(expenses[0], expenses) == True


def test__is_subscription__false_more_than_one_expense_in_month_for_same_service(generate_expense, amount, card, spent_in, 
                                expenses_data_subscription, datetime_now):
    expenses = []
    for record in expenses_data_subscription:
        expenses.append(generate_expense(amount, card, record['spent_in'], record['spent_at']))
    expenses.append(generate_expense(amount, card, spent_in, datetime_now))

    assert is_subscription(expenses[0], expenses) == False


def test__is_subscription__false_wrong_expense(generate_expense, amount, card, expenses_data_subscription, datetime_now):
    expenses = []
    for record in expenses_data_subscription:
        expenses.append(generate_expense(amount, card, record['spent_in'], record['spent_at']))
    expense = generate_expense(amount, card, 'mvideo', datetime_now)

    assert is_subscription(expense, expenses) == False
