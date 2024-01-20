from functions.level_4.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field
import pytest



@pytest.mark.parametrize(
        'config_data,result',
        [
            ('extra_fields = name: str', {'name': str}),
            ('extra_fields: name: str', {'name': str}),
            ('extrafields: name: str', {}),
        ]
)
def test__fetch_extra_fields_configuration__get_first_row_or_none(create_config, config_data, result):
    filepath = create_config(config_data)
    assert fetch_extra_fields_configuration(filepath) == result


def test__fetch_extra_fields_configuration__bad_format_argument_raise_indexerror(create_config):
    filepath = create_config('extra_fields = name')
    with pytest.raises(IndexError):
        fetch_extra_fields_configuration(filepath)


@pytest.mark.xfail(reason='get only first patameter, correct template for ini??')
def test__fetch_extra_fields_configuration__multi_fields(create_config):
    filepath = create_config('extra_fields = name: str\nage: int')
    assert fetch_extra_fields_configuration(filepath) == {'name': str, 'age': int} 
