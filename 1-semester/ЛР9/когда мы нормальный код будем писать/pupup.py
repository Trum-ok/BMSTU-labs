"""
Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и В
"""

from utils import print_matrix


class IncompatibilityError(Exception):
    def __str__(self) -> str:
        return "Количество столбцов матрицы A должно быть равно количеству строк матрицы B для умножения."


def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Умножает две матрицы A и B, возвращая результирующую матрицу C."""
    num_rows_a = len(A)
    num_cols_a = len(A[0]) if A else 0
    num_rows_b = len(B)
    num_cols_b = len(B[0]) if B else 0

    if num_cols_a != num_rows_b:
        # raise ValueError("Количество столбцов матрицы A должно быть равно количеству строк матрицы B для умножения.")
        raise IncompatibilityError  # своя ошибка иначе будет возвращаться ValueError c неправильным текстом

    C = [[0] * num_cols_b for _ in range(num_rows_a)]

    # умножение матриц
    for i in range(num_rows_a):
        for j in range(num_cols_b):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(num_cols_a))

    return C


def main() -> None:
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

    C = matrix_multiply(A, B)

    print("\nМатрица A:")
    print_matrix(A)
    print("\nМатрица B:")
    print_matrix(B)
    print("\nРезультирующая матрица C = A * B:")
    print_matrix(C)


if __name__ == "__main__":
    try:
        main()
    except IncompatibilityError as e:
        print(e)
    except ValueError:
        print("Ошибка ввода! Пожалуйста, вводите только целые числа.")
    except Exception as e:
        print(f"Непредвиденная ошибка: \n{e}")
