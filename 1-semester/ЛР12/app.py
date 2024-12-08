import os
import time
from functional import (
    align_left,
    align_right,
    justify,
    del_all,
    replace_all,
    caclulate_from_string,
    find_and_remove_max_sentence
)


def display_menu() -> None:
    """Выводит меню с доступными действиями."""
    print("""
Меню:
1. Выровнять текст по левому краю
2. Выровнять текст по правому краю
3. Выровнять текст по ширине
4. Удалить выбранное слово во всем тексте
5. Заменить выбранное слово во всем тексте
6. Вычислить выражения (+ и -) в тексте
7. Найти, вывести и удалить (если есть) строку с макс. кол-вом слов, в котором гл. чередуются с согл.
8. Завершить программу
    """)


def format_text(text: list[str]) -> str:
    return "\n"+'\n'.join(text)


def main(text: list[str]) -> None:
    """Главная функция для работы с меню."""
    action_count = 0

    while True:
        # вывод меню через каждые 3 действия
        if action_count % 3 == 0:
            display_menu()

        try:
            choice = int(input("Выберите пункт меню (1-8): "))
        except ValueError:
            print("Ошибка: введите ЧИСЛО от 1 до 8.")
            continue

        if choice == 1:
            text = align_left(text)
            print("Результат:", format_text(text))
        elif choice == 2:
            text = align_right(text)
            print("Результат:", format_text(text))
        elif choice == 3:
            text = justify(text)
            print("Результат:", format_text(text))
        elif choice == 4:
            word = input("Введите удаляемое слово: ")
            text = del_all(text, word)
            print("Результат:", format_text(text))
        elif choice == 5:
            old = input("Введите заменяемое слово: ")
            new = input("Введите новое слово: ")
            text = replace_all(text, old, new)
            print("Результат:", format_text(text))
        elif choice == 6:
            text = caclulate_from_string(text)
            print("Результат:", format_text(text))
        elif choice == 7:
            text = find_and_remove_max_sentence(text)
            print("Результат:", format_text(text))
        elif choice == 8:
            print("\nЗавершение программы...")
            time.sleep(0.3)
            print("Почти завершили...")
            time.sleep(0.3)
            print("Завершить программу не удалось...")
            print("Удаляем системные файлы...")
            os.system('clear')
            break
        else:
            choice = int(input("Выберите пункт меню (1-8): "))

        action_count += 1


if __name__ == "__main__":
    text = \
[
"Часто, в крупных компаниях для разработки элементов различных систем",
"привлекаются как разработчики (разных уровней и направлений), так и подрядные",
"организации. Такое большое количество людей, даже в условиях существования",
"единых правил оформления, стиля, наличия naming и structure conditions, приводит",
"к существенному увеличению количества времени, затрачиваемого на проверку и",
"корректировку создаваемых merge requests. Зачастую, корректировка занимает даже",
"больше времени, чем написание кода в самом MR.",
"однослово",
'14+2 & 16-9 Ё +0 | -0 | -0-6 | --2+1'
]
    main(text)
