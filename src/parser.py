from abc import ABC, abstractmethod

import requests


class Base(ABC):

    @abstractmethod
    def __get_data(self):
        pass

    @abstractmethod
    def get_vacancies(self, word):
         pass



class HeadHunterAPI(Base):
    "Класс для парсинга данных с hh.ru"

    def __init__(self):
        self.__base_url = 'https://api.hh.ru/vacancies'


    def _Base__get_data(self):
        """Имплементируем абстрактный метод __get_data() из Base"""
        return self.__get_data()


    def __get_data(self):
        """Проверка статус-кода ответа"""
        response = requests.get(self.__base_url)
        if response.status_code == 200:
            return 'https://api.hh.ru/vacancies'
        else:
            return "Error"


    def get_vacancies(self, word: str) -> list:
        """Получаем вакансии по заданному слову"""
        url = HeadHunterAPI._Base__get_data(self)
        if url != "Error":
            params = {'text': word.lower(),
                      "per_page": 100}
            response = requests.get(url, params=params).json()
            return response["items"]








