from functions.level_4.four_lines_counter import count_lines_in
import pytest


def test__count_lines_in__filepath_is_directory():
    assert count_lines_in('tests/level_4/') == None


@pytest.mark.parametrize(
        'lines,len_lines',
        [
            (['1\n', '2\n', '3\n'], 3),
            (['1\n', '#2\n', '3\n'], 2),
            (['#1\n', '#2\n', '#3\n'], 0),
            ([], 0),
            (['1'], 1),
        ]
)
def test__count_lines_in__right_len_lines(create_file_with_lines, lines, len_lines):
    filepath = create_file_with_lines(lines)

    assert count_lines_in(filepath) == len_lines
