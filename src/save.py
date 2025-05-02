import json
import os
from abc import ABC, abstractmethod
from typing import Dict, List


class AbstractWorkWithVacancy(ABC):
    """Абстрактный класс, содержащий методы, добавляющие вакансии в файл, получающие данные из файла по
     указанным критериям"""

    @abstractmethod
    def _load_data(self, vacancies: list[dict]) -> list[dict]:
        pass

    @abstractmethod
    def write_data(self, requirements: dict):
        pass



class JSONFileHandler(AbstractWorkWithVacancy):
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vacancies.json")
    def __init__(self, absolute_json_file_path):
        self.__path = absolute_json_file_path


    def _load_data(self) -> List[Dict]:
        """Приватный метод загрузки данных из JSON-файла."""
        try:
            with open(self.__path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")  # Обработка всех ошибок
            return []  # Возвращаем пустой список

    def write_data(self, data_: List[Dict]) -> None:
        """Приватный метод сохранения данных в JSON-файл."""
        try:
            with open(self.__path, "w", encoding="utf-8") as file:
                json.dump(data_, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

