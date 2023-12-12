from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('title', 4) == 'title'
    assert change_copy_item(10, 10) == 10
    assert change_copy_item(None, 10) == None
    assert change_copy_item('Copy of book', 5) == 'Copy of book'
    assert change_copy_item('Copy of book') == 'Copy of book (2)'
    assert change_copy_item('Copy of book (4)') == 'Copy of book (5)'
    assert change_copy_item('Copy of book (d)') == 'Copy of book (d) (2)'
