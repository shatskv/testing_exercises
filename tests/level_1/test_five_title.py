from functions.level_1.five_title import change_copy_item


def test__change_copy_item__no_copy_of_book_little_length():
    assert change_copy_item('title', 4) == 'title'


def test__change_copy_item__no_str_copy_of_books_only_title():
    assert change_copy_item('title') == 'Copy of title'


def test__change_copy_item__have_str_copy_of_book_little_length():
    assert change_copy_item('Copy of book', 5) == 'Copy of book'

    
def test__change_copy_item__have_str_copy_of_book_without_copies():
    assert change_copy_item('Copy of book') == 'Copy of book (2)'


def test__change_copy_item__have_str_copy_of_books_with_copies_in_brackets_int():
    assert change_copy_item('Copy of book (4)') == 'Copy of book (5)'


def test__change_copy_item__have_str_copy_of_books_with_copies_in_brackets_str():
    assert change_copy_item('Copy of book (d)') == 'Copy of book (d) (2)'
