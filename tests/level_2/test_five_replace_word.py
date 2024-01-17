import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    'replace_from, replace_to, expected_result', 
    [
        ('лена', 'Катя', 'Катя пошла в магазин. Катя убралась. Катя сделала задания. Катя пошла спать.'),
        ('Лена', 'Катя', 'Катя пошла в магазин. Катя убралась. Катя сделала задания. Катя пошла спать.'),
        ('Яна', 'Катя', 'Лена пошла в магазин. Лена убралась. Лена сделала задания. Лена пошла спать.'),
    ]
)
def test__replace_word(replace_from, replace_to, expected_result, default_text):
    new_words = replace_word(default_text, replace_from, replace_to)
    assert new_words == expected_result
