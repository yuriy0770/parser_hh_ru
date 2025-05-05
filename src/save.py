import json
import os
from abc import ABC, abstractmethod


class AbstractWorkWithVacancy(ABC):
    """Абстрактный класс, содержащий методы, добавляющие вакансии в файл, получающие данные из файла по
    указанным критериям и удаляющие информацию о вакансии"""

    @abstractmethod
    def _load_data(self) -> None:
        """Абстрактный метод, получающий заданную информацию из вакансии"""
        pass

    @abstractmethod
    def add_vacancies(self, requirements: dict):
        """Абстрактный метод предполагающий добавление новых вакансий в JSON файл"""
        pass


class JSONFileHandler(AbstractWorkWithVacancy):
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vacancies.json")

    def __init__(self, absolute_json_file_path):
        self.__path = absolute_json_file_path
        self.all_data = []
        self._load_data()

    def _load_data(self) -> None:
        """Метод загрузки данных из JSON-файла."""
        try:
            with open(self.__path, "r", encoding="utf-8") as file:
                self.all_data = json.load(file)
        except FileNotFoundError:
            self.all_data = []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            self.all_data = []

    def write_to_file(self, data):
        """Метод записи данных"""
        with open(self.__path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))

    def add_vacancies(self, data_: list[dict]) -> list:
        """Метод добавления данных в JSON-файл."""
        try:
            values_data = [values_d["name"] for values_d in self.all_data]
            d_data = [data for data in data_ if data["name"] not in values_data]
            self.all_data.extend(d_data)
            self.write_to_file(self.all_data)
            return self.all_data
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")
        return []

    def del_vacancy(self):
        """Удаляет все вакансии"""
        with open(self.__path, "w", encoding="utf-8") as f:
            f.write(json.dumps([], ensure_ascii=False, indent=4))
