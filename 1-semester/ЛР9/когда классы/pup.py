"""
Даны две матрицы A и B, в которых количество столбцов одинаково.
Подсчитать для каждого столбца матрицы А количество элементов,
больших среднего арифметического элементов соответствующего
столбца матрицы В. Вывести полученные значения. Затем преобразовать
матрицу В путем умножения всех элементов столбца матрицы на посчитанное
для этого столбца значение, если оно ненулевое. Вывести преобразованную
матрицу в виде матрицы
"""

from utils import print_matrix


def column_means(matrix: list[list[float]]) -> list[float]:
    """Вычисляет среднее арифметическое каждого столбца матрицы
    ## Args:
    - matrix `list[list[float]]` - исходная матрица
    ## Returns:
    - `list[float]` - среднее арифметическое каждого столбца матрицы
    """
    num_cols = len(matrix[0])
    means = [sum(row[col] for row in matrix) / len(matrix) for col in range(num_cols)]
    return means


def count_elements_above_mean(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[int]:
    """
    Подсчитывает для каждого столбца матрицы A количество элементов,
    которые больше среднего соответствующего столбца матрицы B
    ## Args:
    - matrix_a `list[list[float]]` - исходная матрица A
    - matrix_b `list[list[float]]` - исходная матрица B
    ## Returns:
    - `list[int]` - количество элементов в каждом столбце матрицы A,
    которые больше среднего соответствующего столбца матрицы B
    """
    means_b = column_means(matrix_b)
    counts = [
        sum(1 for row in matrix_a if row[col] > means_b[col])
        for col in range(len(means_b))
    ]
    return counts


def transform_matrix(matrix: list[list[float]], counts: list[int]) -> list[list[float]]:
    """Преобразует матрицу путем умножения всех элементов столбца на соответствующее значение counts[i]
    ## Args:
    - matrix `list[list[float]]` - матрица, которую необходимо преобразовать
    - counts ``list[int]` - количество элементов в каждом столбце матрицы A,
    которые больше среднего соответствующего столбца матрицы B
    ## Returns:
    - `list[list[float]]` - преобразованная матрица
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            count = counts[col]
            if count != 0:
                matrix[row][col] *= count


if __name__ == "__main__":
    A = []
    B = []

    rows_a, cols_a = map(int, input("Введите размеры n m матрицы A через пробел: ").split())
    rows_b, cols_b = map(int, input("Введите размеры n m матрицы B через пробел: ").split())

    print("Введите элементы матрицы A построчно:")
    for _ in range(rows_a):
        A.append(list(map(int, input().split())))
    print("Введите элементы матрицы B построчно:")
    for _ in range(rows_b):
        B.append(list(map(int, input().split())))

    # вычисление количества элементов больше среднего в каждом столбце
    counts = count_elements_above_mean(A, B)
    print("Количество элементов в каждом столбце матрицы A, превышающих среднее в B:", counts)

    # преобразование матрицы B
    transformed_matrix_b = transform_matrix(B, counts)
    print("Преобразованная матрица B:")
    print_matrix(transformed_matrix_b)
