import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    'url, result', 
    [
        ('https://github.com/Pupkin/fastapi_weather/pull/1', True),
        ('https://github.com/Pupkin/fastapi_weather/pull/1/8', False),
        ('https:/github.com\\Pupkin/fastapi_weather/pull/1/8', False),
        ('https://gitlab.com/Pupkin/fastapi_weather/pull/1', False),
        ('https://gitlab.com/Pupkin/fastapi_weather/push/1', False)
    ]
)
def test__is_github_pull_request__all_variants(url, result):
    assert is_github_pull_request_url(url) == result
