"""
- Мам, можно мне:
`import numpy as np
X = np.array([[0]])
X.T` ?
- У нас есть `X.T` дома!

Также X.T дома:
"""

def main(X: list[list[int]], n: int) -> list[list[int]]:
    """Транспонирование квадратной матрицы на месте"""
    for i in range(n):
        for j in range(i + 1, n):  # проход только над главной диагональю
            X[i][j], X[j][i] = X[j][i], X[i][j]

    return X


if __name__ == "__main__":
    n, m = 0, 0

    while n <= 0 or m <= 0 or n != m:
        m, n = map(int, input("Введите количество строк и столбцов через пробел: ").split())
        if m <= 0 or n <= 0:
            print("Размер матрицы должен быть положительным!")
        elif n != m:
            raise print("Матрица должна быть квадратной!")

    X = []
    for _ in range(m):
        a = []
        while len(a) != n:
            a = list(map(int, input(f"Введите элементы {_+1}-й строки матрицы через пробел: ").split()))

            if len(a) != n:
                print("Количество столбцов матрицы должно быть идентичным!")

        X.append(a)

    print("Исходная матрица...")
    for i in range(m):
        for j in range(n):
            print(f"{X[i][j]:^15g}", end = ' ')
        print()

    res = main(X, n)

    print()
    for i in range(m):
        for j in range(n):
            print(f"{res[i][j]:^15g}", end = ' ')
        print()
