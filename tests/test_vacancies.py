import pytest

from src.vacancies import Vacancy


def test_vacancy_init():
    name = "Test Vacancy"
    url = "http://example.com/test"
    salary_from = 6000
    salary_to = 12000
    description = "Test Description"

    vacancy = Vacancy(name=name, url=url, salary_from=salary_from, salary_to=salary_to, requirements=description)

    assert vacancy.name == name
    assert vacancy.url == url
    assert vacancy.salary_from == salary_from
    assert vacancy.salary_to == salary_to
    assert vacancy.requirements == description


def test_vacancy_comparison_lt(vacancy, vacancy_system):
    assert vacancy_system < vacancy
    assert not vacancy < vacancy_system


def test_vacancy_comparison_gt(vacancy_system, vacancy):
    assert vacancy_system < vacancy


def test_vacancy_str_method(capsys, vacancy):
    print(vacancy)
    captured = capsys.readouterr()
    expected_output = "Вакансия: Python_developer, зарплата: от 100000 до 120000, URL-адрес: https://hh.ru/applicant/vacancy_response?vacancyId=117286365, Описание: Разработка и поддержка, back end части веб-приложений.\n"
    assert captured.out == expected_output

def test_str_method(vacancy):
    """Тест на строковое отображение вакансии"""

    assert (
        str(vacancy)
        == "Вакансия: Python_developer, зарплата: от 100000 до 120000, URL-адрес: https://hh.ru/applicant/vacancy_response?vacancyId=117286365, Описание: Разработка и поддержка, back end части веб-приложений."
    )


def test_without_name():
    with pytest.raises(ValueError):
        Vacancy(name="",
        url="https://hh.ru/applicant/vacancy_response?vacancyId=117286365",
        salary_from=100000,
        salary_to=120000,
        requirements="Разработка и поддержка, back end части веб-приложений.",)

def test_without_url():
    with pytest.raises(ValueError):
        Vacancy(name="Python_developer",
        url="",
        salary_from=100000,
        salary_to=120000,
        requirements="Разработка и поддержка, back end части веб-приложений.",)

def test_without_url2():
    with pytest.raises(ValueError):
        Vacancy(name="Python_developer",
        url="hh.ru/applicant/vacancy_response?vacancyId=117286365",
        salary_from=100000,
        salary_to=120000,
        requirements="Разработка и поддержка, back end части веб-приложений.",)


def test_from_platform(platform_data):
    vacancies = Vacancy.cast_to_object_list(platform_data)
    assert len(vacancies) == 2

    for i in vacancies:
        assert isinstance(i, Vacancy)

    assert vacancies[0].name == "Программист"
    assert vacancies[0].url == "https://example.com/job1"
    assert vacancies[0].salary_from == 80000
    assert vacancies[0].salary_to == 150000
    assert vacancies[0].requirements == "Описание не указано"
    assert vacancies[1].name == "Тестировщик"
    assert vacancies[1].url == "https://example.com/job2"
    assert vacancies[1].salary_from == 60000
    assert vacancies[1].salary_to == 100000
    assert vacancies[1].requirements == "Описание не указано"

def test___gt__():
    salary_from1 = 50000
    salary_to1 = 70000
    salary_from2 = 60000
    salary_to2 = 80000

    vacancy1 = Vacancy("Test Name 1", "http://test.url1", salary_from1, salary_to1, [])
    vacancy2 = Vacancy("Test Name 2", "http://test.url2", salary_from2, salary_to2, [])

    assert (vacancy1 > vacancy2) == ((salary_from1 + salary_to1) / 2 > (salary_from2 + salary_to2) / 2)