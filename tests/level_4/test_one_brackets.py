import pytest

from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize(
    'name,result',
    [
        ('{ name }', 'name'),
        ('{ name', 'na'),
        ('{name', 'a'),
        ('name', 'name'),
        ('n', 'n'),
        ('name }', 'name }'),
        ('( name )', '( name )')
    ]
)
def test__delete_remove_brackets_quotes__right(name, result):
    assert delete_remove_brackets_quotes(name) == result


def test__delete_remove_brackets_quotes__empty_str_raises_indexerror():
    name = ''
    with pytest.raises(IndexError):
        delete_remove_brackets_quotes(name)
