from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize(1, 0, 'male') == 1
    assert genderalize(1, 0, 'df') == 0
    assert genderalize('male', 'female', 'male') == 'male'
    assert genderalize(None, 'female', 'male') == None
