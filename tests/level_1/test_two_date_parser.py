from datetime import datetime, timedelta

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test__compose_datetime__bad_format_time_exc_valuerror():
    with pytest.raises(ValueError):
        compose_datetime_from('tomorrow', '12.15')


def test__compose_datetime__date_yesterday():
    datetime_now = datetime.now()

    datetime_today = compose_datetime_from('yesterday', '12:15')
    
    assert datetime_today  == datetime(datetime_now.year, datetime_now.month, datetime_now.day, 12, 15, 0)


def test__compose_datetime__date_tomorrow():
    datetime_tomorrow = datetime.now() + timedelta(days=1)

    result_datetime_tomorrow = compose_datetime_from('tomorrow', '12:15')

    assert result_datetime_tomorrow == datetime(datetime_tomorrow.year, datetime_tomorrow.month,
                                                             datetime_tomorrow.day, 12, 15, 0)
