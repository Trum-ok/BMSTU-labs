"""
Лабораторная работа No12 “Текстовый процессор”
Артамонов Аркадий ИУ7-16Б

Программа для замены всех вхождений заданного слова на указанное.
"""

def is_bukva(bukva: str) -> bool:
    return bukva in "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"


def is_word_boundary(prev_char: str, next_char: str) -> bool:
    """
    Проверяет, находятся ли символы на границах слова.

    Аргументы:
        prev_char (str): Символ перед словом.
        next_char (str): Символ после слова.
    Возврат:
        bool: True, если границы корректны.
    """
    return (not prev_char or not is_bukva(prev_char)) and (not next_char or not is_bukva(next_char))


def replace_all(lines: list[str], word: str, new_word: str) -> list[str]:
    """
    Заменяет выбранное слово во всем тексте целиком.

    Аргументы:
        lines (list[str]): Исходный текст в виде списка строк.
        word (str): Слово, которое нужно заменить во всем тексте.
        new_word (str): Слово, на которое производится замена.
    Возврат:
        list[str]: Текст с замененным словом.
    """
    if not word.strip():
        return lines

    word = word.lower()

    for i in range(len(lines)):
        line = lines[i]
        result = []
        start = 0

        while start < len(line):
            idx = line.lower().find(word, start)
            if idx == -1:
                result.append(line[start:])
                break

            prev_char = line[idx - 1] if idx > 0 else ''
            next_char = line[idx + len(word)] if idx + len(word) < len(line) else ''

            if is_word_boundary(prev_char, next_char):
                result.append(line[start:idx])
                result.append(new_word)
                start = idx + len(word)
            else:
                result.append(line[start:idx + len(word)])
                start = idx + len(word)

        lines[i] = ''.join(result)

    return lines


if __name__ == "__main__":
    # from _text import t
    w = input("Введите слово, которое хотите заменить: ")
    # nw = input("Введите слово, на которое хотите заменить: ")
    # print('\n'.join(t))
    # print()
    # print('\n'.join(replace_all(t, w, nw)))
