from datetime import datetime, timedelta

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    datetime_now = datetime.now()
    datetime_tomorrow = datetime_now + timedelta(days=1)
    assert compose_datetime_from(None, '12:15') == datetime(datetime_now.year, datetime_now.month, datetime_now.day,
                                                            12, 15, 0)
    assert compose_datetime_from('tomorrow', '12:15') == datetime(datetime_tomorrow.year, datetime_tomorrow.month,
                                                             datetime_tomorrow.day, 12, 15, 0)
    
    
def test_compose_datetime_from_exceptions():
    with pytest.raises(ValueError):
        compose_datetime_from('tomorrow', '12.15')
    with pytest.raises(Exception):
        compose_datetime_from(None, None)
