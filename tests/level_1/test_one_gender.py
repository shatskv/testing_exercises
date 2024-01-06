from functions.level_1.one_gender import genderalize


def test__genderalize__is_male():
    assert genderalize('male', 'female', 'male') == 'male'


def test__genderalize__is_female():
    assert genderalize('male', 'female', 'female') == 'female'


def test__genderalize__is_female_with_wrong_gender():
    assert genderalize('male', 'female', '1male') == 'female'
