from unittest.mock import patch

from src.parser import HeadHunterAPI, Base


def test1(api_len):
    api = api_len
    assert len(api.get_vacancies('python')) == 100


def test2():
    assert issubclass(HeadHunterAPI, Base)


def test3(api_len):
    api = api_len
    q = api.get_vacancies("python")
    assert "python" in str(q)
    assert "salary_range" in str(q)
    assert "name" in str(q)


def test_get_vacancies_success():
    """Тест на успешное получение вакансий."""
    with patch("requests.get") as mock_get:
        # Мокаем успешный ответ от API с вакансией
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": [{"id": 1, "name": "Developer"}]}
        q = HeadHunterAPI()
        vacancies = q.get_vacancies("developer")
        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Developer"


def test_hh_api_init():
    q = HeadHunterAPI()
    assert q._HeadHunterAPI__base_url == "https://api.hh.ru/vacancies"


