"""
Лабораторная работа No12 “Текстовый процессор”
Артамонов Аркадий ИУ7-16Б

Программа выровнивает текст по левому краю.
"""


def align_left(lines: list[str]) -> list[str]:
    """
    Выравнивание текста по левому краю.

    Аргументы:
        lines (list[str]): Исходный текст.
    Возврат:
        list[str]: Выровненный по левому краю текст.
    """
    return [(" ".join(line.split())) for line in lines]


if __name__ == "__main__":
    from _text import t
    print('\n'.join(align_left(t)))
