import pytest

from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__all_coefficient_same_root():
    a = 9
    b = -30
    c = 25

    result = solve_square_equation(a, b, c)

    assert result[0] == result[1] and round(result[0], 2) == 1.67


@pytest.mark.parametrize(
    'a,b,c,result',
    [
        (2, 5, -3, (-3.0, 0.5)),
        (0, 15, -30, (2.0, None)),
        (25, 50, 0, (-2.0, 0.0)),
        (25, 0, 0, (0.0, 0.0)),
        (1, 1, 25, (None, None))
    ]
)
def  test__solve_square_equation__all_roots(a, b, c, result):
    assert solve_square_equation(a, b, c) == result
