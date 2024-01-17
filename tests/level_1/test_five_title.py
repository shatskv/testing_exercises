from functions.level_1.five_title import change_copy_item
import pytest

def test__change_copy_item__return_title_without_copy_of_book_for_little_max_length_title():
    assert change_copy_item('title', 4) == 'title'


def test__change_copy_item__no_str_copy_of_books_for_only_title_without_copy_of():
    assert change_copy_item('title') == 'Copy of title'


def test__change_copy_item__not_increase_copy_of_number_for_little_max_length_title():
    assert change_copy_item('Copy of book', 5) == 'Copy of book'


@pytest.mark.parametrize(
        'title,result', 
        [
            ('Copy of book', 'Copy of book (2)'),
            ('Copy of book (4)', 'Copy of book (5)'),
            ('Copy of book (d)', 'Copy of book (d) (2)')
        ]
)
def test__change_copy_item__increase_copy_number(title, result):
    assert change_copy_item(title) == result
