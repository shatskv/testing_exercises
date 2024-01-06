from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__all_coefficient_all_roots():
    a = 2
    b = 5
    c = -3

    result = solve_square_equation(a, b, c)

    assert result == (-3.0, 0.5)


def test__solve_square_equation__all_coefficient_same_root():
    a = 9
    b = -30
    c = 25

    result = solve_square_equation(a, b, c)

    assert result[0] == result[1] and round(result[0], 2) == 1.67


def test__solve_square_equation__only_b_c_coefficients_one_root():
    a = 0
    b = 15
    c = -30

    result = solve_square_equation(a, b, c)

    assert result[0] == 2.0 and result[1] is None


def test__solve_square_equation__only_a_b_coefficientstwo_root():
    a = 25
    b = 50
    c = 0

    result = solve_square_equation(a, b, c)

    assert result == (-2.0, 0.0)


def test__solve_square_equation__only_a_coefficients_two_zero_roots():
    a = 25
    b = 0
    c = 0

    result = solve_square_equation(a, b, c)

    assert result == (0.0, 0.0)


def test__solve_square_equation__all_coefficienst_no_roots():
    a = 1
    b = 1
    c = 25

    result = solve_square_equation(a, b, c)

    assert result == (None, None)
