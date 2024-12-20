def main(X: list[list[int]], m: int) -> int:
    """Индекс строки с наибольшим средним арифметическим"""
    idx = 0
    mean = float("-inf")

    for i in range(m):
        s = sum(X[i])
        if s > mean:  # можно не делить
            idx = i
            mean = s

    return idx


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

    res = main(X, m)
    print(f"{res+1}-я строка матрицы имеет наибольшее среднее арифметическое")
