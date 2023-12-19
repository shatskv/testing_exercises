import pytest

from functions.level_2.three_first import NOT_SET, first


def test__first__return_first():
    items = [5, 4, 5, 6]

    item = first(items)

    assert item == items[0]


def test__first__empty_list_return_none():
    items = []

    item = first(items, None)

    assert item == None


def test__first__empty_list_return_int():
    items = []
    default = 1

    item = first(items, default)

    assert item == default


def test__first__empty_list_return_str():
    items = []
    default = 'dffdfdf'

    item = first(items, default)

    assert item == default


def test__first__default_not_set_exc_attribute_error():
    items = []

    with pytest.raises(AttributeError):
        first(items, NOT_SET)
