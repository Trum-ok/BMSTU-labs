"""
Лабораторная работа №2 'Написание алгоритмов с выбором условий'
Артамонов Аркадий ИУ7-16Б
Задание 3

Программа для определения принадлежности точки (x, y) 
к заданной области (учитывая границы)
"""


def y1(x: float) -> float:
    return -1/8 * (x - 9)**2 + 8


def y2(x: float) -> float:
    return 7 * (x - 8)**2 + 1


def y3(x: float) -> float:
    return 1/49 * (x - 1)**2


def y4(x: float) -> float:
    return -4 * x**2 + 2


def y5(x: float) -> float:
    return 4 * x**2 - 6


def y6(x: float) -> float:
    return -1/16 * x**2


def y7(x: float) -> float:
    return -2 * (x - 1)**2 - 2


def y8(x: float) -> float:
    return 1/3 * (x - 5)**2 - 7


def check(x: float, y: float) -> bool:
    """Проверяет принадлежность точки к области"""
    if y >= 0:
        if x > 9:
            return False
        if x >= 8:
            return (y >= y2(x)) and (y1(x) >= y)
        elif x >= 1 and x <= 8:
            if (y3(x) <= y) and (y1(x) >= y):
                return True
            else:
                return y == 1.5*(x) + 2
        elif x >= 0 and x <= 1:
            return (y == 1.5*(x) + 2) or ((y >= y5(x)) and (y <= y4(x)))
    else:
        if x > 8:
            return False
        if x >= 2:
            return (y >= y8(x)) and (y <= y6(x))
        elif x >= 1:
            return (y >= y7(x)) and (y <= y6(x))
        elif x >= 0 and x <= 1:
            return (y >= y5(x)) and (y <= y4(x))
    return False


if __name__ == '__main__':
    x = abs(float(input('Введите x: ')))
    y = float(input('Введите y: '))

    if check(x, y):
        print('Точка принадлежит')
    else:
        print('Точка не принадлежит')
