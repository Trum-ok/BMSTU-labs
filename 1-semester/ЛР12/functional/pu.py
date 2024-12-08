"""
Лабораторная работа No12 “Текстовый процессор”
Артамонов Аркадий ИУ7-16Б

Программа выровнивает текст по правому краю.
"""


def align_right(lines: list[str]) -> list[str]:
    """
    Выравнивание текста по правому краю.

    Аргументы:
        lines (list[str]): Исходный текст.
    Возврат:
        list[str]: Выровненный по правому краю текст.
    """
    max_length = max(len(line) for line in lines)
    for i in range(len(lines)):
        s = " ".join(lines[i].split())
        space_needed = max_length - len(s)
        lines[i] = space_needed * " " + s
    return lines


if __name__ == "__main__":
    from _text import t
    print('\n'.join(align_right(t)))
