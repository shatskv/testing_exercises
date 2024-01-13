import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import (
    guess_expense_category, is_string_contains_trigger)


@pytest.mark.parametrize(
    'original_string, trigger, result', [
        (' apple', 'apple', True),
        (',apple', 'apple', True),
        ('.apple', 'apple', True),
        ('-apple', 'apple', True),
        ('/apple', 'apple', True),
        ('\\apple', 'apple', True),
        ('-apple/', 'apple', True),
    ]
)
def test__is_string_contains_trigger__all_rigth_delimiters(original_string, trigger, result):
    assert is_string_contains_trigger(original_string, trigger) == result


@pytest.mark.parametrize(
    'original_string, trigger, result', [
        ('apple', 'apple', True),
        (',APPLE', 'apple', True),
        ('apple,', 'apple', True),
        (',apple,', 'apple', True),
    ]
)
def test__is_string_contains_trigger__all_rigth_postions_delimeter(original_string, trigger, result):
    assert is_string_contains_trigger(original_string, trigger) == result


@pytest.mark.parametrize(
    'original_string, trigger, result', [
        ('apple', 'apple3', False),
        ('apple3', 'apple', False),
        ('*apple', 'apple', False),
        ('$apple,', 'apple', False),
        ('@apple,', 'apple', False),
    ]
)
def test__is_string_contains_trigger__wrong_delimeter_and_trigers(original_string, trigger, result):
    assert is_string_contains_trigger(original_string, trigger) == result


@pytest.mark.parametrize(
    'spent_in,result', [
        ('asAdor,', ExpenseCategory.BAR_RESTAURANT),
        (',sas,', ExpenseCategory.SUPERMARKET),
        ('-netflix,', ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        ('/farm/,', ExpenseCategory.MEDICINE_PHARMACY),
        (' tomsarkgh,', ExpenseCategory.THEATRES_MOVIES_CULTURE),
        ('yandex go,', ExpenseCategory.TRANSPORT),
    ])
def test__guess_expense_category__all_categories_right(generate_expense, amount, card, spent_in, datetime_now, result):
    expense = generate_expense(amount, card, spent_in, datetime_now)

    assert guess_expense_category(expense) == result


@pytest.mark.parametrize(
    'spent_in,result', [
        ('asa1dor,', None),
        (',s1as,', None),
        ('-net1flix,', None),
        ('/far1m/,', None),
        (' toms1arkgh,', None),
        ('yand1ex go,', None),
    ])
def test__guess_expense_category__bad_spent_in_return_none(generate_expense, amount, card, spent_in, datetime_now, result):
    expense = generate_expense(amount, card, spent_in, datetime_now)

    assert guess_expense_category(expense) == result
