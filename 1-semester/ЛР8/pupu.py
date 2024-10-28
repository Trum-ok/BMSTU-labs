def main(X: list[list[int]], m: int, n: int) -> list[list[int]]:
    """Перестановка столбцов с максимальной и минимальной суммой элементов"""
    max_sum_idx = 0
    max_sum = 0
    min_sum_idx = 0
    min_sum = 0

    for i in range(n):
        cnt = sum(X[k][i] for k in range(m))
        if cnt > max_sum:
            max_sum = cnt
            max_sum_idx = i
        elif min_sum > cnt:
            min_sum = cnt
            min_sum_idx = i
        cnt = 0

    for _ in range(m):
        X[_][min_sum_idx], X[_][max_sum_idx] =  X[_][max_sum_idx], X[_][min_sum_idx]

    return X


if __name__ == "__main__":
    n, m = 0, 0

    while n <= 0 or m <= 0:
        m, n = map(int, input("Введите количество строк и столбцов через пробел: ").split())
        if m <= 0 or n <= 0:
            print("Размер матрицы должен быть положительным!")

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

    res = main(X, m, n)

    print()
    for i in range(m):
        for j in range(n):
            print(f"{res[i][j]:^15g}", end = ' ')
        print()
