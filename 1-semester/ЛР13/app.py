import os
import sys
from db import (
    add_new_record,
    initialize_db,
    display_db,
    search_by_one_field,
    search_by_two_fields
)
from colorama import Fore, Style


def main() -> None:
    file_path = None
    separator = None
    os.system('clear')
    print(Fore.LIGHTCYAN_EX + "\nДобро пожаловать в cassandra-macro-mini-micro!" + Style.RESET_ALL)

    while True:
        print("\nМеню:")
        if file_path is None:
            print(Fore.LIGHTGREEN_EX + "1. Выбрать файл для работы <-- Сначала выберете файл" + Style.RESET_ALL)
        else:
            print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись в базу данных")
        print("5. Поиск по одному полю")
        print("6. Поиск по двум полям")
        print(Fore.LIGHTRED_EX + "7. Выйти" + Style.RESET_ALL)

        choice = input("Введите номер действия: ")
        if not choice.isdigit():
            print(Fore.LIGHTRED_EX + "\nВведите НОМЕР выбраного пункта из меню!\n" + Style.RESET_ALL)
            continue

        if int(choice) in list(range(2, 6+1)) and file_path is None:
            print(Fore.LIGHTRED_EX + "\nСначала выберите файл!\n" + Style.RESET_ALL)
            continue

        if choice == '1':
            file_path = input("Введите путь к файлу: ")
            if file_path.endswith('.csv'):
                separator = ','
            elif file_path.endswith('.psv'):
                separator = '|'
            else:
                separator = input("Введите разделитель (по умолчанию ','): ")
            if separator is None:
                separator = ','
            if not os.path.exists(rf"./user_tables/{file_path}"):
                print(Fore.LIGHTYELLOW_EX + "Файл не существует. Он будет создан при инициализации." + Style.RESET_ALL)
            else:
                print(Fore.LIGHTGREEN_EX + "Таблица найдена"  + Style.RESET_ALL)
        elif choice == '2':
            num_records = int(input("Введите количество записей: "))
            records = []
            for _ in range(num_records):
                record = input(f"Введите запись (через {separator}): ").split(separator)
                records.append(record)
            initialize_db(file_path, records, separator)
            print(Fore.LIGHTGREEN_EX + "База данных инициализирована."  + Style.RESET_ALL)
        elif choice == '3':
            display_db(file_path, separator)
        elif choice == '4':
            record = input("Введите запись (через запятую): ").split(',')
            add_new_record(file_path, record)
            print("Запись добавлена.")
        elif choice == '5':
            field_index = int(input("Введите номер поля для поиска (с 0): "))
            value = input("Введите значение для поиска: ")
            search_by_one_field(file_path, field_index, value)
        elif choice == '6':
            field1_index = int(input("Введите номер первого поля (с 0): "))
            value1 = input("Введите значение первого поля: ")
            field2_index = int(input("Введите номер второго поля (с 0): "))
            value2 = input("Введите значение второго поля: ")
            search_by_two_fields(file_path, field1_index, value1, field2_index, value2)
        elif choice == '7':
            print(Fore.LIGHTCYAN_EX + "Выход из программы." + Style.RESET_ALL)
            break
        else:
            print(Fore.LIGHTRED_EX + "\nНеверный ввод. " + Style.RESET_ALL + "Попробуйте снова.")


if __name__ == "__main__":
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     print(Fore.LIGHTCYAN_EX + "\nВыход из программы." + Style.RESET_ALL)
    #     sys.exit(0)
    # except Exception as e:
    #     print(Fore.RED + "\nПроизошла ошибка:" + Style.RESET_ALL)
    #     print(Fore.YELLOW + f"{type(e).__name__}: {e}" + Style.RESET_ALL)
    #     sys.exit(1)
    main()
