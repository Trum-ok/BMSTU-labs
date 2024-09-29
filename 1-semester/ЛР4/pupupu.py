"""
Лабораторная работа №4 'Сумма бесконечного ряда'
Артамонов Аркадий ИУ7-16Б (44 Вариант)

Программа для вычисления суммы бесконечного ряда:
y = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!
"""

from typing import Tuple


def main(x: float, epsilon: float, its: int, step: int) -> Tuple[float, int]:
    """Вычисление суммы бесконечного ряда"""

    term = x  # 1-ый член ряда
    sum_series = term  # сумма ряда
    factorial = 1  # начальный факториал 1!
    n = 1  # счетчик нечётных степеней (2n+1)
    iteration = 1

    print("-" * 39)
    print(f"| {'№ итерации':^10} | {'t':^10} | {'s':^10} |")
    print("-" * 39)
    print(f"| {iteration:<10} | {term:^10.5g} | {sum_series:^10.5g} |")

    # итерации + таблица
    while (abs(term) > epsilon) and (iteration < its):
        factorial *= (2*n) * (2*n + 1)  # n-ый факториал (для оптимизации)
        term = x**(2*n + 1) / factorial  # n-ый член ряда
        sum_series += term  # обновление счетчика суммы
        n += 1
        iteration += 1

        if (iteration % step == 1) or (step == 1):
            print(f"| {iteration:<10} | {term:^10.5g} | {sum_series:^10.5g} |")
    print("-" * 39)

    if (abs(term) < epsilon):
        return -1, -1

    return sum_series, iteration


if __name__ == "__main__":
    x = float(input("Введите значение x: "))
    epsilon = float(input("Введите значение ε: "))
    its = int(input("Введите количество итераций: "))
    step = int(input("Введи шаг вывода: "))
    result, iterations = main(x, epsilon, its, step)

    if iterations == -1:
        print(f'За указанное число итераций ({its}) необходимой точности достичь не удалось.')
    else:
        print(f"Сумма бесконечного ряда - {result:.5g}, вычислена за {iterations} итераций.")
