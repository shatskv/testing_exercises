import string

import pytest

from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize(
        'len_promocode',
        [
            (5), (0), (10), (-5), (20)
        ]
)
def test__generate_promocode_right(len_promocode):
    promocode = generate_promocode(len_promocode)

    assert len(promocode) == (len_promocode if len_promocode and len_promocode >= 0 else 0)
    assert all(char in string.ascii_uppercase for char in promocode)


def test__generate_promocode__len_promocode_is_none():
    len_promocode = 8
    promocode = generate_promocode(len_promocode)

    assert len(promocode) == len_promocode
    assert all(char in string.ascii_uppercase for char in promocode)
