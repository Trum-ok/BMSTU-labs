from typing import Tuple


def main(x: float, epsilon: float) -> Tuple[float, int]:
    term = x
    sum_series = term
    n = 1
    iteration = 1
    st = 1
    fact = 1

    print(f"| {iteration:<10} | {term:^12.5g} | {sum_series:^10.5g} |")

    while (abs(term) > epsilon):
        fact *= (n+1)*(n+2)
        n += 2
        term = ((x**n) / fact) * (-1)**(st)
        sum_series += term

        print(f"| {iteration:<10} | {term:^12.5g} | {sum_series:^10.5g} | {fact:^13} | {x**(n)}")

        st += 1
        iteration += 1

    return sum_series


if __name__ == "__main__":
    x = float(input("Введите значение x: "))
    epsilon = float(input("Введите значение ε: "))
    result = main(x, epsilon)
    print(f"Сумма бесконечного ряда - {result:.7g}")
