def main(X: list[list[int]], m: int, n: int) -> tuple[int, int]:
    """Поиск столбца, имеющего наибольшее количество простых чисел"""
    idx = 0
    max_prime_count = 0

    for i in range(n):
        cnt = 0  # счетчик в текущем столбце

        for j in range(m):
            num = X[j][i]
            if num > 1:
                is_prime = True
                for k in range(2, int(num**0.5) + 1):
                    if num % k == 0:
                        is_prime = False
                        break
                if is_prime:
                    cnt += 1

        if cnt > max_prime_count:
            max_prime_count = cnt
            idx = i

    return idx, max_prime_count



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

    idx, cnt = main(X, m, n)
    if cnt == 0:
        print("Столбец с простыми числами не найден")
    else:
        print(f"Столбец, имеющий наибольшее количество простых чисел: {idx}")
