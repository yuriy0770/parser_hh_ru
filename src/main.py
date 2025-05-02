import os
from parser import HeadHunterAPI
from save import JSONFileHandler
from vacancies import Vacancy


def main():
    hh_api = HeadHunterAPI()
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "vacancies.json")
    storage = JSONFileHandler(absolute_json_file_path)

    if not hh_api._Base__get_data():
        print("Не удалось подлкючиться к API сайта hh.ru")


    query = input("Введите поисковой запрос: ")
    vacancies = hh_api.get_vacancies(query)
    storage.write_data(vacancies) if storage else None
    print(f'Добавили {len(vacancies)} вакансий')



    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    data = storage._load_data() if storage else None
    vacancies_list = Vacancy.cast_to_object_list(data)

    sorted_vacancies = sorted(vacancies_list,
        key=lambda x: (x.salary_from if x.salary_from is not None else 0 + x.salary_to if x.salary_to is not None else 0) / 2,
        reverse=True)
    for i in sorted_vacancies[:top_n]:
        print(i.__str__())



if __name__ == "__main__":
    main()


   


