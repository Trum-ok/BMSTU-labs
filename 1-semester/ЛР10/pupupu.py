"""
Лабораторная работа №10: Вычисление приближённого значения интеграла
Артамонов Аркадий ИУ7-16Б
Назначение: программа для вычисления интеграла функции двумя методами с оценкой точности.
(Метод правых треугольников и метод трапеций)
"""

import math
from typing import Optional

# Функция для вычисления значений интегрируемой функции f(x)
def f(x) -> float:
    return math.sin(x)  # Пример функции

# Функция для вычисления первообразной F(x)
def F(x) -> float:
    return -math.cos(x)  # Первообразная функции f(x) = sin(x)


def right_rectangle_method(a: float, b: float, n: int) -> float:
    """
    Метод правых прямоугольников ([a, b])
    #### Args:
        a: float - начало отрезка интегрирования
        b: float - конец
        n: int - количество участков разбиения (прямоугольников)
    #### Returns:
        float - ~значение интеграла
    """
    h = (b - a) / n
    result = sum(f(a + i * h) for i in range(1, n + 1)) * h
    return result


def trapezoid_method(a: float, b: float, n: int) -> float:
    """
    Метод трапеций
    #### Args:
        a: float - начало отрезка интегрирования
        b: float - конец
        n: int - количество участков разбиения (трапеций)
    #### Returns:
        float - ~значение интеграла
    """
    h = (b - a) / n
    result = (f(a) + f(b)) / 2 + sum(f(a + i * h) for i in range(1, n))
    result *= h
    return result


def absolute_error(I_approx: float, I_exact: float) -> float:
    """Абсолютная ошибка"""
    return abs(I_approx - I_exact)


def relative_error(I_approx, I_exact) -> Optional[float]:
    """Относительная ошибка (%)"""
    if I_exact == 0:
        return None
    return abs((I_approx - I_exact) / I_exact) * 100


def main() -> None:
    # ввод значений
    try:
        a = float(input("Введите начало отрезка интегрирования (a): "))
        b = float(input("Введите конец отрезка интегрирования (b): "))
        N1 = int(input("Введите количество участков разбиения N1: "))
        N2 = int(input("Введите количество участков разбиения N2: "))
    except ValueError:
        print("Ошибка: введены некорректные данные!")
        return

    I_exact = F(b) - F(a)  # точное значение интеграла по первообразной

    # вычисления для N1
    try:
        I1 = right_rectangle_method(a, b, N1)
    except ZeroDivisionError:
        I1 = None  # недопустимое разбиение для метода правых прямоугольников

    try:
        I3 = trapezoid_method(a, b, N1)
    except ZeroDivisionError:
        I3 = None  # недопустимое разбиение для метода трапеций

    # вычисления для N2
    try:
        I2 = right_rectangle_method(a, b, N2)
    except ZeroDivisionError:
        I2 = None

    try:
        I4 = trapezoid_method(a, b, N2)
    except ZeroDivisionError:
        I4 = None

    # вывод таблицы
    print("\nТаблица результатов:")
    print(f"{'N':<5} {'Метод 1 (правые прямоугольники)':<30} {'Метод 2 (трапеции)':<30}")
    print(f"{'N1':<5} {I1:<30.7g} {I3:<30.7g}")
    print(f"{'N2':<5} {I2:<30.7g} {I4:<30.7g}")

    # оценка погрешностей
    for i, (I, n) in enumerate([(I1, N1), (I2, N2), (I3, N1), (I4, N2)], start=1):
        if I is not None:
            abs_err = absolute_error(I, I_exact)
            rel_err = relative_error(I, I_exact)
            print(f"\nМетод {1 if i <= 2 else 2}, N{1 if i % 2 != 0 else 2}:")
            print(f"Абсолютная погрешность: {abs_err:.7g}")
            print(f"Относительная погрешность: {rel_err:.7g}%")

    # определение наилучшего метода
    methods = ((I1, "Метод 1, N1"), (I2, "Метод 1, N2"), (I3, "Метод 2, N1"), (I4, "Метод 2, N2"))
    best_method = min(methods, key=lambda x: absolute_error(x[0], I_exact) if x[0] is not None else float('inf'))
    print(f"\nНаиболее точный метод: {best_method[1]}")

    # уточнение количества отрезков для менее точного метода
    epsilon = float(input("Введите требуемую точность ε: "))
    method_name = "Метод правых прямоугольников" if best_method[1].startswith("Метод 2") else "Метод трапеций"
    n = N2 if best_method[1].endswith("N1") else N1
    I_old = best_method[0]

    while True:
        n *= 2
        if method_name == "Метод правых прямоугольников":
            I_new = right_rectangle_method(a, b, n)
        else:
            I_new = trapezoid_method(a, b, n)

        if abs(I_new - I_old) < epsilon:
            break
        I_old = I_new

    print(f"\nДля метода '{method_name}' достигнута точность {epsilon:.7g} при n = {n}")
    print(f"Приближенное значение интеграла: {I_new:.7g}")


if __name__ == "__main__":
    main()
