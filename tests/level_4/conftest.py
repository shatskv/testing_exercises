import pytest
from functions.level_4.two_students import Student
import string
import random
from typing import Callable
import os
import time

@pytest.fixture
def students() -> list[Student]:
    return [
        Student('John', 'Doe', '@johndoe'),
        Student('Jane', 'Doe', '@janedoe'),
        Student('Alice', 'Smith', None),
        Student('Bob', 'Johnson', '@bobjohnson'),
        Student('Charlie', 'Brown', '@charliebrown')
    ]


@pytest.fixture
def generate_random_string() -> Callable[[int], str]:
    def _generate_random_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
    return _generate_random_string


@pytest.fixture
def generate_random_student(generate_random_string) -> Callable[[str], Student]:
    def _generate_random_student(nickname):
        name = generate_random_string(6)
        surname  = generate_random_string(6)
        student = Student(name, surname, f'@{nickname}')
        return student
    return _generate_random_student


@pytest.fixture
def filepath_txt():
    return 'tests/level_4/test_file.txt'


@pytest.fixture
def filepath_ini():
    return 'tests/level_4/test_config.ini'


@pytest.fixture
def create_file_with_lines(filepath_txt) -> Callable[[list[str]], filepath_txt]:
    def _create_file_with_lines(lines):
        with open(filepath_txt, 'w') as file:
            file.writelines(lines)
        return filepath_txt
        
    yield _create_file_with_lines
    os.remove(filepath_txt)


@pytest.fixture
def create_config(filepath_ini) -> Callable[[str], filepath_ini]:
    def _create_config(data):
        file_data = '[tool:app-config]\n' + data
        with open(filepath_ini, 'w') as file:
            file.write(file_data)
        return filepath_ini
        
    yield _create_config
    os.remove(filepath_ini)
