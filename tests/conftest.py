import os
from unittest.mock import MagicMock, patch

import pytest
from src.parser import HeadHunterAPI
from src.save import JSONFileHandler
from src.vacancies import Vacancy


@pytest.fixture
def api_len():
    return HeadHunterAPI()


@pytest.fixture
def json_file_handler():
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vac.json")
    return JSONFileHandler(absolute_json_file_path)

@pytest.fixture
def vacancy():
    return Vacancy(
        name="Python_developer",
        url="https://hh.ru/applicant/vacancy_response?vacancyId=117286365",
        salary_from=100000,
        salary_to=120000,
        requirements="Разработка и поддержка, back end части веб-приложений.",
    )


@pytest.fixture
def vacancy_system():
    return Vacancy(
        name="Системный администратор",
        url="https://hh.ru/applicant/vacancy_response?vacancyId=112451122",
        salary_from=50000,
        salary_to=90000,
        requirements="Разработка и поддержка, back end части веб-приложений."
    )


@pytest.fixture()
def platform_data():
    return [
        {
            "name": "Программист",
            "apply_alternate_url": "https://example.com/job1",
            "salary": {"from": 80000, "to": 150000},
            "requirements": {"name": "Описание не указано"},
        },
        {
            "name": "Тестировщик",
            "apply_alternate_url": "https://example.com/job2",
            "salary": {"from": 60000, "to": 100000},
            "requirements": {"name": "Описание не указано"},
        },
    ]

