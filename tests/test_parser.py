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

