import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
        'params,result',
        [
            ({'id': '56'}, 'google.com/account?id=56'),
            ({'id': '56', 'user': 'desar'}, 'google.com/account?id=56&user=desar'),
            ({}, 'google.com/account'),
        ]
)
def test__build_url__successfully(urls, params, result):
    host, relative_url = urls
    assert build_url(host, relative_url, params) == result



def test__build_url__bad_params_raise_attributeerror():
    with pytest.raises(AttributeError):
        build_url('google.com', 'account', 12)
