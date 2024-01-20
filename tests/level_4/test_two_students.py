import pytest

from functions.level_4.two_students import Student, get_student_by_tg_nickname


@pytest.mark.parametrize(
        'nickname,result', 
        [
            ('janedoe', Student('Jane', 'Doe', '@janedoe')),
            ('charliebrown', Student('Charlie', 'Brown', '@charliebrown')),
            ('charlie111brown', None),
        ]
)
def test__get_student_by_tg_nickname_right(students, nickname, result):
    assert get_student_by_tg_nickname(nickname, students) == result


@pytest.mark.parametrize(
        'nickname,result', 
        [
            ('janedoe', Student('Jane', 'Doe', '@janedoe')),
            ('charliebrown', Student('Charlie', 'Brown', '@charliebrown')),
        ]
)
def test__get_student_by_tg_nickname_more_than_two_matched_students(students, nickname, result, generate_random_student):
    students.append(generate_random_student(nickname))
    assert get_student_by_tg_nickname(nickname, students) == result
