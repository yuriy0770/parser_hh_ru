
from typing import List, Dict
from urllib.parse import urlparse

class Vacancy:
    __slots__ = ("name", "url", "salary_from", "salary_to", 'requirements')
    def __init__(self, name, url, salary_from, salary_to, requirements):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirements = requirements
        self.__validate()

    def __str__(self) -> str:
        return f'Вакансия: {self.name}, зарплата: от {self.salary_from} до {self.salary_to}, URL-адрес: {self.url}, Описание: {self.requirements}'

    def __validate(self, ):
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Название должно быть строкой и не пустым")
        if not isinstance(self.url, str) and self.url != "":
            raise ValueError("URL должен быть строкой и не пустой строчкой")
        parsed_url = urlparse(self.url)
        if not (parsed_url.scheme in ['http', 'https'] and parsed_url.netloc):
            raise ValueError("Допустимые URL: http(s)://<domain>")


    def __lt__(self, other: "Vacancy") -> bool:
        """Метод, сравнивающий вакансии по минимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 < (other.salary_from + other.salary_to) / 2

    def __gt__(self, other: "Vacancy") -> bool:
        """Метод, сравнивающий вакансии по максимальной ЗП"""
        return (self.salary_from + self.salary_to) / 2 > (other.salary_from + other.salary_to) / 2

    @staticmethod
    def cast_to_object_list(vacancies: List[Dict]) -> List:
        """Преобразовываем набор данных из JSON в список объектов"""
        result = []
        for i in vacancies:
            name = i.get("name", "Название не указано")
            url = i.get("apply_alternate_url")
            salary_from = i.get("salary", {}).get("from", 0) if i.get("salary") else 0
            salary_to = i.get("salary", {}).get("to", 0) if i.get("salary") else 0

            department = i.get("snippet")
            description = department.get("responsibility", "Описание не указано") if department else "Описание не указано"

            vacancy = Vacancy(name=name, url=url, salary_from=salary_from, salary_to=salary_to,
                              requirements=description)

            result.append(vacancy)

        return result

