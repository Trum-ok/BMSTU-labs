"""
Задана матрица D и массив I, содержащий номера строк,
для которых необходимо определить максимальный элемент.
Значения максимальных элементов запомнить в массиве R.
Определить среднее арифметическое вычисленных максимальных значений.
Напечатать матрицу D, массивы I и R, среднее арифметическое значение
"""

from utils import print_matrix


def mean(a: list[float]) -> float:
    return sum(a) / len(a)


def find_max_in_rows(matrix: list[list[float]], rows: list[int]) -> list[float]:
    """Ищет максимальное значение в строке rows[i] и добавляет в список"""
    r = []
    [r.append(max(matrix[row-1])) for row in rows]
    return r


def main() -> None:
    n, m = map(int, input("Введите размеры матрицы n-строк и m-столбцов через пробел: ").split(' '))

    if n == 0 or m == 0:
        raise ValueError("Матрица должна иметь натуральные размеры!")

    D = []
    ids = list(map(int, input("Введите номера строк через пробел: ").split(' ')))

    if len(ids) == 0:
        raise ValueError("Массив должен быть не пустым!")

    for i in range(n):
        D.append(list(map(int, input(f"Введите элементы {i + 1} строки через пробел: ").split(' '))))

    r = find_max_in_rows(D, ids)
    mod_r = []
    mod_r.extend(r)
    for i in range(n):
        if i+1 not in ids:
            mod_r.insert(i, "-")

    mean_r = mean(r)

    print("\nМатрица D и максимальное значение указанных строк")
    print_matrix(D, side_info=mod_r)
    print(f"Массив I: {ids}")
    print(f"Массив R: {r}")
    print(f"Среднее арифметическое значений R: {mean_r}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Непредвиденная ошибка: \n{e}")
