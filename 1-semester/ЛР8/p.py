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
    m, n = map(int, input("Введите количество строк и столбцов через пробел: ").split())
    if m <= 0 or n <= 0:
        raise ValueError("Размер матрицы должен быть положительным!")

    X = []
    for _ in range(m):
        a = list(map(int, input(f"Введите элементы {_+1}-й строки матрицы через пробел: ").split()))

        if len(a) != n:
            raise ValueError("Количество столбцов матрицы должно быть идентичным!")

        X.append(a)

    res = main(X, m)
    print(f"{res+1}-я строка матрицы имеет наибольшее среднее арифметическое")
