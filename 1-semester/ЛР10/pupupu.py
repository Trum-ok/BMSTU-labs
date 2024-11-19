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
    result = 0.0
    for i in range(1, n + 1):
        result += f(a + i * h)
    return result * h


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
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h


def absolute_error(I_approx: float, I_exact: float) -> float:
    """Абсолютная ошибка"""
    return abs(I_approx - I_exact)


def relative_error(I_approx: float, I_exact: float) -> Optional[float]:
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

        if a == b:
            print("Ошибка: начало и конец отрезка не могут быть одинаковыми!")
            return
        elif (a > b) and (a < 0):
            print("Ошибка: начало отрезка не может быть больше конца!")
            return
        elif a > b and b < 0:
            print("Ошибка: начало отрезка не может быть больше конца!")
            return
        if N1 <= 0 or N2 <= 0:
            print("Количество разбиений должно быть натуральным числом!")
            return
    except ValueError:
        print("Ошибка: введены некорректные данные!")
        return

    I_exact = F(b) - F(a)  # точное значение интеграла по первообразной

    I1 = right_rectangle_method(a, b, N1)
    I3 = trapezoid_method(a, b, N1)
    I2 = right_rectangle_method(a, b, N2)
    I4 = trapezoid_method(a, b, N2)

    # вывод таблицы
    print("\nТаблица результатов:")
    print(f"{'N':<5} {'Метод 1 (правые прямоугольники)':<30} {'Метод 2 (трапеции)':<30}")
    print(f"{'N1':<5} {I1:<30.7g} {I3:<30.7g}")
    print(f"{'N2':<5} {I2:<30.7g} {I4:<30.7g}")

    # оценка погрешностей
    for i, (I, n) in enumerate([(I1, N1), (I2, N2), (I3, N1), (I4, N2)], start=1):
        abs_err = absolute_error(I, I_exact)
        rel_err = relative_error(I, I_exact)
        print(f"\nМетод {1 if i <= 2 else 2}, N{1 if i % 2 != 0 else 2}:")
        if abs_err is not None:
            print(f"Абсолютная погрешность: {abs_err:.7g}")
        else:
            print("Деление на ноль")
        if rel_err is not None:
            print(f"Относительная погрешность: {rel_err:.7g}%")
        else:
            print("Деление на ноль")

    # определение наилучшего метода
    methods = ((I1, "Метод 1, N1"), (I2, "Метод 1, N2"), (I3, "Метод 2, N1"), (I4, "Метод 2, N2"))
    best_method = min(methods, key=lambda x: absolute_error(x[0], I_exact) if x[0] is not None else float('inf'))
    print(f"\nНаиболее точный метод: {best_method[1]}")

    # уточнение количества отрезков для менее точного метода
    epsilon = float(input("Введите требуемую точность ε: "))
    method_name = "Метод правых прямоугольников" if best_method[1].startswith("Метод 1") else "Метод трапеций"
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
