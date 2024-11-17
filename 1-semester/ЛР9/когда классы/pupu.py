from utils import print_matrix


def mean(a: list[float]) -> float:
    """Вычисляет среднее арифметическое списка a"""
    return sum(a) / len(a)


def find_max_in_rows(matrix: list[list[float]], rows: list[int]) -> list[float]:
    """Ищет максимальные значения в заданных строках и сохраняет их в список"""
    return [max(matrix[row - 1]) for row in rows]


def main() -> None:
    n, m = map(int, input("Введите размеры матрицы n-строк и m-столбцов через пробел: ").split())

    D = [list(map(int, input(f"Введите элементы {i + 1} строки через пробел: ").split())) for i in range(n)]
    ids = list(map(int, input("Введите номера строк через пробел: ").split()))

    r = find_max_in_rows(D, ids)
    mod_r = [r[ids.index(i + 1)] if (i + 1) in ids else "-" for i in range(n)]
    mean_r = mean(r)

    print("\nМатрица D и максимальные значения указанных строк")
    print_matrix(D, side_info=mod_r)
    print(f"Массив I: {ids}")
    print(f"Массив R: {r}")
    print(f"Среднее арифметическое значений R: {mean_r}")


if __name__ == "__main__":
    main()
