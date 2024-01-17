import pytest

from functions.level_2.three_first import NOT_SET, first

@pytest.mark.parametrize("items, default, expected_result", [
    ([5, 4, 5, 6], None, 5),
    ([], None, None),
    ([], 1, 1),
    ([], 'dffdfdf', 'dffdfdf'),
])
def test__first__successfully(items, default, expected_result):
    assert first(items, default) == expected_result


def test__first__default_not_set_exc_attribute_error():
    items = []

    with pytest.raises(AttributeError):
        first(items, NOT_SET)
