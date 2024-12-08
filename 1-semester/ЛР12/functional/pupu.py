"""
Лабораторная работа No12 “Текстовый процессор”
Артамонов Аркадий ИУ7-16Б

Программа для удаления всех вхождений заданного слова.
"""


def del_all(lines: list[str], word: str) -> list[str]:
    """
    Удаляет выбранное слово во всем тексте.

    Аргументы:
        lines (list[str]): Исходный текст.
        word (str): Слово, которое нужно удалить во всем тексте.
    Возврат:
        list[str]: Текст без введенного слова.
    """
    if not word.strip():
        return lines

    for i in range(len(lines)):
        lines[i] = lines[i].replace(f" {word} ", '')
        lines[i] = lines[i].replace(f" {word}\n", '')
        if lines[i][:-1].endswith(f" {word}") and lines[i][-1] in [",", '.', '!', '?', ':', ';']:
            lines[i] = lines[i].replace(f" {word}", '')
        if lines[i].startswith(f"{word} "):
            lines[i] = lines[i].replace(f"{word} ", '')
    return lines
