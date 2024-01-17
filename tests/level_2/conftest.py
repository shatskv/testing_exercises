import pytest


@pytest.fixture
def words():
    return {'кот', 'собака'}, {'дурак', 'крыса', 'идиоты'}


@pytest.fixture
def short_text():
    return 'Дурак кот собака стул стол идиоты Крыса'


@pytest.fixture
def long_text():
    return 'Дурак кот собака стул Cобака стол идиоты Крыса'


@pytest.fixture
def default_text():
    return 'Лена пошла в магазин. Лена убралась. Лена сделала задания. Лена пошла спать.'
