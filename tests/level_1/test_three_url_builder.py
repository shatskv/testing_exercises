import pytest

from functions.level_1.three_url_builder import build_url


def test__build_url__one_param_str():
    assert build_url('google.com', 'account', {'id': '56'}) == 'google.com/account?id=56'


def test__build_url__multi_params():
    assert build_url('google.com', 'account', {'id': '56', 'user': 'desar'}) == \
                                        'google.com/account?id=56&user=desar'
    

def test__build_url__no_params():
    assert build_url('google.com', 'account', {}) == 'google.com/account'


def test__build_url__bad_params_raise_attributeerror():
    with pytest.raises(AttributeError):
        build_url('google.com', 'account', 12)
