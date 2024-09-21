"""
Лабораторная работа №2 'Написание алгоритмов с выбором условий'
Артамонов Аркадий ИУ7-16Б

Программа для решения квадратных уравнений
"""


# 0. Импорт ф-ии из модуля
from math import sqrt
from typing import Tuple, Optional


# 1. Определение ф-ии для подсчета корней (если таковые имеются)
def main(a: float, b: float, c: float) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    if a != 0:
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
            return x1, x2, None
        elif D == 0:
            x = -b / (2*a)
            return x, None, None
        else:
            return None, None, 'Решений нет'
    else:
        if b == 0:
            if c == 0:
                return None, None, "х - любое"
            else:
                return None, None, 'Решений нет, график - прямая y = c параллельная Ox'
        else:
            x = -c / b
            return x, None, None


# 2. Запуск программы
if __name__ == '__main__':
    # 3. Ввод коэффициентов
    a = float(input('Введите значение коэффициента a: '))
    b = float(input('Введите значение коэффициента b: '))
    c = float(input('Введите значение коэффициента c: '))

    # 4. Вызов ф-ии
    x1, x2, msg = main(a, b, c)
    # 5. Вывод результата
    if msg is None:
        if x2 is None:
            print(f'x = {x1:5f}')
        else:
            print(f'x1 = {x1:5f} \nx2 = {x2:5f}')
    else:
        print(msg)
