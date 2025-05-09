from abc import ABC, abstractmethod

import requests


class Base(ABC):

    @abstractmethod
    def _get_data(self):
        pass

    @abstractmethod
    def get_vacancies(self, word):
        pass


class HeadHunterAPI(Base):
    """Класс для парсинга данных с hh.ru"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.session = None

    @property
    def get_data(self):
        """Возвращаем статус код"""
        return self._get_data()

    def _get_data(self):
        """Проверка статус-кода ответа"""
        response = requests.get(self.__base_url)
        if response.status_code == 200:
            self.session = requests.Session()

    def get_vacancies(self, word: str) -> list:
        """Получаем вакансии по заданному слову"""
        self._get_data()
        if self.session:
            params = {"text": word.lower(), "per_page": 100}
            response = requests.get(self.__base_url, params=params)
            if response.status_code == 200:
                try:
                    data = response.json()["items"]
                except Exception as err:
                    raise err
                return data
            return []
        else:
            print("Подключение не удалось.")
        return []
