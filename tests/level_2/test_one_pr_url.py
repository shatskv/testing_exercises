from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request__url_is_true():
    url = 'https://github.com/Pupkin/fastapi_weather/pull/1'

    is_github_pull = is_github_pull_request_url(url)

    assert is_github_pull == True


def test__is_github_pull_request__url_is_false_len_8():
    url = 'https://github.com/Pupkin/fastapi_weather/pull/1/8'

    is_github_pull = is_github_pull_request_url(url)

    assert is_github_pull == False


def test__is_github_pull_request__url_is_false_bad_slashes():
    url = 'https:/github.com\\Pupkin/fastapi_weather/pull/1/8'

    is_github_pull = is_github_pull_request_url(url)

    assert is_github_pull == False


def test__is_github_pull_request__url_is_false_not_github():
    url = 'https://gitlab.com/Pupkin/fastapi_weather/pull/1'

    is_github_pull = is_github_pull_request_url(url)

    assert is_github_pull == False


def test__is_github_pull_request__url_is_false_not_pull():
    url = 'https://gitlab.com/Pupkin/fastapi_weather/push/1'

    is_github_pull = is_github_pull_request_url(url)

    assert is_github_pull == False
