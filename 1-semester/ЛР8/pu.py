def main(X: list[list[int]], m: int) -> list[list[int]]:
    """Перестановка строки с наибольшим и наименьшим количеством отрицательных элементов"""
    imic = [0, 0] #  индекс | количество
    imac = [0, 0] #  индекс | количество
    cnt = 0

    for i in range(m):
        for j in X[i]:
            if j < 0:
                cnt += 1
        if cnt < imic[1]:
            imic[0] = i
            imic[1] = cnt
        elif imac[1] < cnt:
            imac[0] = i
            imac[1] = cnt
        cnt = 0

    X[imic[0]], X[imac[0]] = X[imac[0]], X[imic[0]]
    return X


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

    print("Исходная матрица...")
    for i in range(m):
        for j in range(n):
            print(f"{X[i][j]:^15g}", end = ' ')
        print()

    res = main(X, m)

    print()
    for i in range(m):
        for j in range(n):
            print(f"{res[i][j]:^15g}", end = ' ')
        print()
