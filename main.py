from src.api_client import ApiClientPlanes
from src.filemanager import JSONAeroplane


def main() -> None:
    """Функция - консольный интерфейс"""

    print("Программа получения данных о самолетах выбранной страны")
    fail_name = input("Введите название файла\n")
    if fail_name == "":
        fail_name = "data/aeroplane.json"
    else:
        fail_name = "data/" + fail_name + ".json"
    api_search = ApiClientPlanes()
    print("Выберете действие:")
    print("1 - загрузка из файла.")
    print("2 - запрос по названию страны.")

    while True:
        choice = input()
        if choice == "1":
            data_load = JSONAeroplane(fail_name).get_planes()
            break
        elif choice == "2":
            country_search = input("Введите название страны\n")
            data_load = api_search.get_aeroplanes(country_search)  # список данных о самолетах
            break
        else:
            print("Неверный ввод (ввести 1 или 2")

    list_plains = api_search.convert_to_aeroplanes(data_load)  # список экземпляров Aeroplane
    for plan in list_plains:
        print(plan)
    print(f"Найдено самолетов - {len(data_load)}.")

    print("Выберете дальнейшие действие с данными:")
    print("1 - Загрузка данных в файл.")
    print("2 - Получить топ N самолетов по высоте полета.")
    print("3 - Получить самолеты по стране их регистрации.")
    print("4 - Удаление данных из файла.")
    print("5 - Выход.")
    while True:
        choice = input()
        if choice == "1":
            data_list = []
            for plane in list_plains:
                data_list.append(plane.to_list())
            JSONAeroplane(fail_name).write_planes(data_load)
            print(f"Данные о {len(list_plains)} самолетах записаны в файл {fail_name}. Выход.")
            break
        elif choice == "2":
            quantity_planes = int(input("Введите количество самолетов для отображения\n"))
            sorted_list = sorted(list_plains, reverse=True)
            if quantity_planes > len(sorted_list):
                quantity_planes = len(sorted_list)
            list_plains = sorted_list[:quantity_planes]
            for plane in sorted_list:
                print(plane)

        elif choice == "3":
            key_word = input("Введите слово для поиска\n").upper()
            sorted_list = []
            for plane in list_plains:
                if key_word in plane.origin_country.upper():
                    sorted_list.append(plane)
                    print(plane)
            list_plains = sorted_list
            print(f"Найдено {len(list_plains)} самолетов")
        elif choice == "4":
            JSONAeroplane().clear_all()
            break

        elif choice == "5":
            print("Выход")
            break
        else:
            print("Неверный ввод (ввести число от 1 до 5)")


if __name__ == "__main__":
    main()
