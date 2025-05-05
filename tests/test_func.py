from src.func import get_sorted_vacancies
from src.parser import HeadHunterAPI
from src.vacancies import Vacancy


def test1():
    q = HeadHunterAPI()
    e = q.get_vacancies("python")
    w = Vacancy.cast_to_object_list(e)


    assert get_sorted_vacancies(w) != w


def test2():
    q = HeadHunterAPI()
    e = q.get_vacancies("python")
    w = Vacancy.cast_to_object_list(e)
    assert len(get_sorted_vacancies(w)) == 100