import os
from typing import NoReturn

from src.parser import HeadHunterAPI
from save import JSONFileHandler
from src.func import get_sorted_vacancies, filter_vacancies
from vacancies import Vacancy


def main() -> NoReturn:
    hh_api = HeadHunterAPI()
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vacancies.json")
    storage = JSONFileHandler(absolute_json_file_path)

    query = input("Введите поисковой запрос: ")
    vacancies = hh_api.get_vacancies(query)
    list_vacancies = [vacancy_.to_dict() for vacancy_ in Vacancy.cast_to_object_list(vacancies)]
    actual_data = storage.add_vacancies(list_vacancies)
    vacancies_list = Vacancy.cast_to_object_list_2(actual_data)
    print(f"Добавили {len(vacancies_list)} уникальных вакансий")

    answer1 = input("Хотите получить вакансии по определенному слову да/нет ")
    if answer1 == "да":
        word = input("Введите слово: ")
        filter_vacancies(vacancies_list, word)
    else:
        print("Как хотите")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    sorted_vacancies = get_sorted_vacancies(vacancies_list)
    for i, j in enumerate(sorted_vacancies[:top_n], start=1):
        print(i, j.__str__())

    answer = input("Хотите удалить какие-то вакансии по номеру да/нет ")
    if answer == "да":
        answer1 = input("Введите номера вакансий которые хотите удалить через пробел(например '1 7')")
        num1, num2 = map(int, answer1.split())
        for i, j in enumerate(sorted_vacancies, start=1):
            if i in range(num1, num2 + 1):
                del sorted_vacancies[i - 1]
            else:
                continue
        print("Список всех вакансий без удаленных")
        for i, j in enumerate(sorted_vacancies, start=1):
            print(f"{i} {j.__str__()}")
    else:
        print("Как хотите")
    delete_all = input("Может вы хотите удалить все вакансии (да/нет) ").lower()
    if delete_all == "да":
        storage.del_vacancy()
        print("Все вскансии удалены")
    else:
        print("Вакансии остались на месте")


if __name__ == "__main__":
    main()
