from utils import print_matrix


def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Умножает две матрицы A и B, возвращая результирующую матрицу C."""
    num_rows_a = len(A)
    num_cols_a = len(A[0]) if A else 0
    num_rows_b = len(B)
    num_cols_b = len(B[0]) if B else 0

    # Проверка совместимости матриц
    if num_cols_a != num_rows_b:
        print("Ошибка: количество столбцов матрицы A должно быть равно количеству строк матрицы B.")
        return []

    # Создание матрицы C
    C = [[sum(A[i][k] * B[k][j] for k in range(num_cols_a)) for j in range(num_cols_b)] for i in range(num_rows_a)]
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
    if C:  # Печатаем результат, только если умножение выполнено
        print("\nМатрица A:")
        print_matrix(A)
        print("\nМатрица B:")
        print_matrix(B)
        print("\nРезультирующая матрица C = A * B:")
        print_matrix(C)


if __name__ == "__main__":
    main()
