"""
Лабораторная работа №2 'Написание алгоритмов с выбором условий'
Артамонов Аркадий ИУ7-16Б

Программа для решения квадратных уравнений
"""


# 0. Импорт ф-ии из модуля
from math import sqrt


# 1. Определение ф-ии для подсчета корней (если таковые имеются)
def main(a: float, b: float, c: float):
    if a == 0 and b == 0 and c == 0:
        print('Решений нет, график - точка')
    elif a != 0:
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
            print(f'Решения уравнения: x1 = {x1:5f}, x2 = {x2:5f}')
        elif D == 0:
            x = -b / (2*a)
            print(f'Решения уравнения: x = {x:5f}')
        else:
            print('Решений нет')
    elif a == 0:
        if b != 0 and c != 0:
            x = -c / b
            print(f'Решение уравнения: x = {x:5f}')
        elif b == 0:
            print('Решений нет, график - прямая y = c параллельная Ox')
        elif c == 0:
            print('Решение уравнения: x = 0')


if __name__ == '__main__':
    a = float(input('Введите значение коэффициента a: '))
    b = float(input('Введите значение коэффициента b: '))
    c = float(input('Введите значение коэффициента c: '))

    main(a, b, c)
