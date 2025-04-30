
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









