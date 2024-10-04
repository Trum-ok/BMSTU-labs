from typing import Tuple


def main(x: float, epsilon: float) -> Tuple[float, int]:
    term = x
    sum_series = term
    n = 1
    iteration = 1
    factorial = 1

    print("+" + "-" * 38 + "+")
    print(f"| {'№ итерации':^10} | {'t':^10} | {'s':^10} |")
    print("+" + "-" * 38 + "+")
    print(f"| {iteration:<10} | {term:^10.5g} | {sum_series:^10.5g} |")

    while abs(term > epsilon):
        factorial *= n
        term = (x ** n) / n
        sum_series += term
        n += 1
        iteration += 1

        print(f"| {iteration:<10} | {term:^10.5g} | {sum_series:^10.5g} |")
    print("+" + "-" * 38 + "+")

    return sum_series, iteration


if __name__ == "__main__":
    x = int(input("Введите значение x: "))
    epsilon = float(input("Введите значение ε: "))
    result, iterations = main(x, epsilon)
    print(f"Сумма бесконечного ряда - {result:.5g}, вычислена за {iterations} итераций.")
