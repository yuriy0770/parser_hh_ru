from typing import List, Dict


class Vacancy:
    __slots__ = ("name", "url", "salary_from", "salary_to", "requirements")

    def __init__(self, name, url, salary_from, salary_to, requirements):
        self.name = Vacancy._validate_str(name)
        self.url = Vacancy._validate_url(url)
        self.salary_from = Vacancy._validate_salary(salary_from)
        self.salary_to = Vacancy._validate_salary(salary_to)
        self.requirements = Vacancy._validate_requirements(requirements)

    def __str__(self) -> str:
        return f"Вакансия: {self.name}, зарплата: от {self.salary_from} до {self.salary_to}, URL-адрес: {self.url}, Описание: {self.requirements}"

    @staticmethod
    def _validate_str(name):
        if isinstance(name, str) and len(name) > 0:
            return name
        elif name == None:
            name = "Вакансия не указана"
            return name
        else:
            raise ValueError(f"{name} - Ошибка валидации!!")

    @staticmethod
    def _validate_url(url):
        if isinstance(url, str) and len(url) > 0:
            return url
        elif url == None:
            url = "url не указано"
            return url
        else:
            raise ValueError(f"{url} - Ошибка валидации!!")

    @staticmethod
    def _validate_requirements(requirements):
        if isinstance(requirements, str) and len(requirements) > 0:
            return requirements
        elif requirements == None:
            requirements = "Описание не указано"
            return requirements
        else:
            raise ValueError(f"{requirements} - Ошибка валидации!!")

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
        for info in vacancies:

            name = info.get("name", "Название не указано").lower()
            url = info.get("apply_alternate_url")
            salary = info.get("salary")

            salary_from = salary["from"] if salary and salary.get("from") else 0
            salary_to = salary["to"] if salary and salary.get("to") else 0

            department = info.get("snippet")
            description = (
                department.get("responsibility")
                if department and department.get("responsibility")
                else "Описание не указано"
            )

            vacancy = cls(name=name, url=url, salary_from=salary_from, salary_to=salary_to, requirements=description)

            result.append(vacancy)
        return result

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirements": self.requirements,
        }

    @classmethod
    def cast_to_object_list_2(cls, data: List[Dict]) -> List["Vacancy"]:
        list_d = []
        for i in data:
            vacancy = cls(
                name=i["name"],
                url=i["url"],
                salary_from=i["salary_from"],
                salary_to=i["salary_to"],
                requirements=i["requirements"],
            )
            list_d.append(vacancy)

        return list_d
