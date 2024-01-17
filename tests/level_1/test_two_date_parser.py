from datetime import datetime, timedelta

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test__compose_datetime__bad_format_time_raise_valuerror():
    with pytest.raises(ValueError):
        compose_datetime_from('tomorrow', '12.15')


def test__compose_datetime__date_yesterday(today):
    

    datetime_today = compose_datetime_from('yesterday', '12:15')
    
    assert datetime_today.date() == today.date()


def test__compose_datetime__right_time():

    datetime_today = compose_datetime_from('today', f'{12}:{43}')

    assert datetime_today.hour == 12
    assert datetime_today.minute == 43


def test__compose_datetime__date_tomorrow(today):
    datetime_tomorrow = today + timedelta(days=1)

    result_datetime_tomorrow = compose_datetime_from('tomorrow', '12:15')

    assert result_datetime_tomorrow == datetime(datetime_tomorrow.year, datetime_tomorrow.month,
                                                             datetime_tomorrow.day, 12, 15, 0)
