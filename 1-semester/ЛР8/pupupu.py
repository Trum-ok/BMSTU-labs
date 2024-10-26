"""
- Мам, можно мне:
`import numpy as np
X = np.array([[0]])
X.T` ?
- У нас есть `X.T` дома!

Также X.T дома:
"""

def main(X: list[list[int]], m: int, n: int) -> list[list[int]]:
    """Транспонирование матрицы"""
    transposed = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            transposed[j][i] = X[i][j]  # X[i][j] на место [j][i]

    return transposed


if __name__ == "__main__":
    m, n = map(int, input("Введите количество строк и столбцов через пробел: ").split())
    if m <= 0 or n <= 0:
        raise ValueError("Размер матрицы должен быть положительным!")

    X = []
    for _ in range(m):
        a = list(map(int, input(f"Введите элементы {_+1}-й строки матрицы через пробел: ").split()))

        if len(a) != n:
            raise ValueError("Количество столбцов матрицы должно быть идентичным!")

        X.append(a)

    res = main(X, m, n)

    print()
    for _ in res:
        print(_)
