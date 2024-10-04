from typing import Tuple
from math import sin, sqrt


def main(epsilon: float) -> Tuple[float, int]:
    n = 1e+15
    term = sin(n**2)*sqrt(n)
    sum_series = term
    iteration = 1

    print(f"| {iteration:<10} | {term:^12.5g} | {sum_series:^10.5g} | {n}")

    while (abs(term) > epsilon):
        n += 1
        term = sin(n**2)*sqrt(n)
        sum_series += term

        print(f"| {iteration:<10} | {term:^12.5g} | {sum_series:^10.5g} | {n}")
        iteration += 1

    return sum_series


if __name__ == "__main__":
    # epsilon = float(input("Введите значение ε: "))
    epsilon = 1e-5
    result = main(epsilon)
    print(f"Сумма бесконечного ряда - {result:.7g}")
