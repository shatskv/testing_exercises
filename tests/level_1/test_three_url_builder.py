import pytest

from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('google.com', 'account', {'id': '56'}) == 'google.com/account?id=56'
    assert build_url('google.com', 'account', {'id': 56}) == 'google.com/account?id=56'
    assert build_url('google.com', 'account', {'id': '56', 'user': 'desar'}) == \
                                        'google.com/account?id=56&user=desar'
    assert build_url('google.com', 'account', None) == 'google.com/account'
    

def test_build_url_exceptions():
    with pytest.raises(AttributeError):
        build_url('google.com', 'account', 12)
