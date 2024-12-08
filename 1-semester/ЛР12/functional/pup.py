"""
Лабораторная работа No12 “Текстовый процессор”
Артамонов Аркадий ИУ7-16Б

Программа выровнивает текст по ширине.
"""
from functional.p import align_left


def justify(lines: list[str]) -> list[str]:
    """
    Выравнивание текста по ширине (максимальная длина строки).

    Аргументы:
        lines (list[str]): Исходный текст.
    Возврат:
        list[str]: Выравненный по ширине текст.
    """
    lines = align_left(lines)
    max_length = max(len(line) for line in lines)

    justified_lines: list[str] = []
    for line in lines:
        if len(line) == max_length:
            justified_lines.append(line)
            continue

        words = line.split()
        if len(words) == 1:
            justified_lines.append(line)
        else:
            spaces_needed = max_length - len(line.replace(' ', ''))
            gaps = len(words) - 1
            space_distribution = [spaces_needed // gaps] * gaps
            for i in range(spaces_needed % gaps):
                space_distribution[i] += 1

            justified_line = ''.join(word + (' ' * space_distribution[i] if i < gaps else '') for i, word in enumerate(words))
            justified_lines.append(justified_line)

    return justified_lines


if __name__ == "__main__":
    from _text import t
    print("\n"+'\n'.join(justify(t))+"\n")
