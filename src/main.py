import os
from turtledemo.penrose import start
from typing import NoReturn

from src.parser import HeadHunterAPI
from save import JSONFileHandler
from src.func import func
from vacancies import Vacancy


def main() -> NoReturn:
    hh_api = HeadHunterAPI()
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vacancies.json")
    storage = JSONFileHandler(absolute_json_file_path)

    query = input("Введите поисковой запрос: ")
    vacancies = hh_api.get_vacancies(query)
    actual_data = storage.add_vacancies(vacancies)
    print(f'Добавили {len(vacancies)} вакансий')

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    vacancies_list = Vacancy.cast_to_object_list(actual_data)
    sorted_vacancies = func(vacancies_list)
    for i, j in enumerate(sorted_vacancies[:top_n], start=1):
        print(i, j.__str__())

    answer = input("Хотите удалить какие-то вакансии по номеру да/нет ")
    if answer == "да":
        answer1 = input("Введите номера вакансий которые хотите удалить через пробел(например '1 7')")
        num1, num2 = map(int, answer1.split())
        for i, j in enumerate(sorted_vacancies,start=1):
            if i in range(num1, num2+1):
                del sorted_vacancies[i-1]
            else:
                continue
        print("Список всех вакансий без удаленных")
        for i,j in enumerate(sorted_vacancies, start=1):
            print(f"{i} {j.__str__()}")
    else:
        print("Как хотите")

if __name__ == "__main__":
    main()

   


