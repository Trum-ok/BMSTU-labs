def main(X: list[list[int]], m: int, n: int) -> tuple[int, int]:
    """
    Поиск максимального значения в квадратной матрице над главной диагональю и
    минимального - под побочной диагональю
    """
    min_el = float('inf')
    max_el = float('-inf')

    for i in range(m):
        for j in range(n):
            if i < j:  # над основной
                if X[i][j] > max_el:
                    max_el = X[i][j]
            if i + j > n - 1:  # под побочной
                if X[i][j] < min_el:
                    min_el = X[i][j]

    return min_el, max_el


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

    min_el, max_el = main(X, m, n)
    print(f"Минимальный элемент: {min_el}, максимальный: {max_el}")
