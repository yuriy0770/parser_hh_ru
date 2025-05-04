from typing import List, Dict
from urllib.parse import urlparse

class Vacancy:
    __slots__ = ("name", "url", "salary_from", "salary_to", 'requirements')
    def __init__(self, name, url, salary_from, salary_to, requirements):
        self.name = Vacancy._validate_str(name)
        self.url = Vacancy._validate_str(url)
        self.salary_from = Vacancy._validate_salary(salary_from)
        self.salary_to = Vacancy._validate_salary(salary_to)
        self.requirements = Vacancy._validate_str(requirements)

    def __str__(self) -> str:
        return f'Вакансия: {self.name}, зарплата: от {self.salary_from} до {self.salary_to}, URL-адрес: {self.url}, Описание: {self.requirements}'

    @staticmethod
    def _validate_str(name):
        if isinstance(name, str) and len(name) > 0:
            return name
        else:
            raise ValueError(f"{name} - Ошибка валидации!!")

    @staticmethod
    def _validate_salary(salary_from):
        if isinstance(salary_from, int | float):
            return salary_from
        return 0

    def __lt__(self, other: "Vacancy") -> bool:
        """Метод, сравнивающий вакансии по минимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 < (other.salary_from + other.salary_to) / 2

    def __gt__(self, other: "Vacancy") -> bool:
        """Метод, сравнивающий вакансии по максимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 > (other.salary_from + other.salary_to) / 2

    @classmethod
    def cast_to_object_list(cls, vacancies: List[Dict]) -> List:
        """Преобразовываем набор данных из JSON в список объектов"""
        result = []
        for i in vacancies:
            name = i.get("name", "Название не указано")
            url = i.get("apply_alternate_url")

            salary_from = 0
            salary_to = 0
            get_salary = i["salary"]
            if get_salary:
                salary_from = get_salary["from"] if get_salary.get("from") else 0
                salary_to = get_salary["to"] if get_salary.get("to") else 0

            department = i.get("snippet")
            description = department.get("responsibility", "Описание не указано") \
                if department and department["responsibility"] else "Описание не указано"
            vacancy = cls(name=name, url=url, salary_from=salary_from, salary_to=salary_to,
                              requirements=description)

            result.append(vacancy)
        return result

    def to_dict(self):
        return {"name": self.name, "url": self.url, "salary_from": self.salary_from,
                "salary_to": self.salary_to, "requirements": self.requirements}