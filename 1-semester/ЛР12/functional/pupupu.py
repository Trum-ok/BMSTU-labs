"""
Лабораторная работа No12 “Текстовый процессор”
Артамонов Аркадий ИУ7-16Б

Программа для вычисление арифметических выражений над целыми числами внутри текста (+ и -).
"""
def calculus(line: str) -> str:
    if len(line) == 0:
        return ""

    line = line.replace("+","👁️🫦👁️")
    line = line.replace("-","👁️🫦👁️-")
    line = line.split("👁️🫦👁️")

    res = sum(int(x) for x in line if x != "")
    if res == 0:
        return "0"
    return f"{res}"


def caclulate_from_string(lines: list[str]) -> list[str]:
    for i in range(len(lines)):
        while " + " in lines[i] or " - " in lines[i]:
            lines[i] = lines[i].replace(" - ", "-").replace(" + ", "+")
        while "++" in lines[i] or "--" in lines[i]:
            lines[i] = lines[i].replace("--", "+").replace("++", "+")
        line = lines[i]
        j = 0
        while j < len(line):
            if line[j] in "-+0123456789":
                start = j
                while j < len(line) and line[j] in "-+0123456789":
                    j += 1
                expression = line[start:j]
                if any(c in "+-" for c in expression[1:]):
                    result = calculus(expression)
                    line = line[:start] + result + line[j:]
                    j = start + len(result) - 1
            j += 1
        lines[i] = line
    return lines


if __name__ == "__main__":
    t = [
    "однослово",
    '14+2 & 16-9 10-2+7 +0 | -0 | -0-6 | --2+1',
    "текст ++6 - 4 был",
    "-4 +5",
    "3 + 5 6 + 3"
    ]
    print('\n'.join(caclulate_from_string(t)))
