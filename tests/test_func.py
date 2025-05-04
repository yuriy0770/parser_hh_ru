from src.func import func
from src.parser import HeadHunterAPI
from src.vacancies import Vacancy


def test():
    q = HeadHunterAPI()
    e = q.get_vacancies("python")
    w = Vacancy.cast_to_object_list(e)


    assert func(w) != w