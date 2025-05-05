from typing import List

from src.vacancies import Vacancy


def get_sorted_vacancies(vacancies):
    """Возвращает вакансии отсортированные по убыванию от средней зарплаты"""
    return sorted(vacancies, reverse=True)


def filter_vacancies(vacancies_list: List[Vacancy], word):
    """Печатает все вакансии по найденному слову"""
    for i in vacancies_list:
        if word in i.name or word in i.requirements:
            print(i.__str__())
