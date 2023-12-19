from functions.level_2.five_replace_word import replace_word


def return_default_text():
    text = 'Лена пошла в магазин. Лена убралась. Лена сделала задания. Лена пошла спать.'
    return text


def test__replace_word__replace_words_replace_from_lowcase():
    text = return_default_text()
    replace_from = 'лена'
    replace_to = 'Катя'

    new_words = replace_word(text, replace_from, replace_to)

    assert new_words == 'Катя пошла в магазин. Катя убралась. Катя сделала задания. Катя пошла спать.'


def test__replace_word__replace_words_replace_from_capitalaze():
    text = return_default_text()
    replace_from = 'Лена'
    replace_to = 'Катя'

    new_words = replace_word(text, replace_from, replace_to)

    assert new_words == 'Катя пошла в магазин. Катя убралась. Катя сделала задания. Катя пошла спать.'


def test__replace_word__replace_words_replace_from_does_not_match():
    text = return_default_text()
    replace_from = 'Яна'
    replace_to = 'Катя'

    new_words = replace_word(text, replace_from, replace_to)

    assert new_words == text
