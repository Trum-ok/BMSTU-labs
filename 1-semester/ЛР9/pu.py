"""
Повернуть квадратную целочисленную матрицу на 90 градусов по часовой стрелке,
затем на 90 градусов против часовой стрелки. Вывести исходную, промежуточную
и итоговую матрицы. Дополнительных матриц и массивов не вводить. Транспонирование не применять.
"""

from matrix_anot import Matrix


def rotate_clockwise(matrix: Matrix, n: int) -> None:
    """Поворот матрицы на 90 градусов по часовой стрелке"""
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # поворот четырех элементов за раз
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp


def rotate_counterclockwise(matrix: Matrix, n: int) -> None:
    """Поворот матрицы на 90 градусов против часовой стрелки"""
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # поворот четырех элементов
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = temp


def main() -> None:
    # ввод исходной матрицы
    n = int(input("Введите размер матрицы: "))
    matrix = Matrix([list(map(int, input().split())) for _ in range(n)])

    print("\nИсходная матрица:")
    print(matrix)

    # поворот на 90 градусов по часовой стрелке
    rotate_clockwise(matrix, n)
    print("\nПосле поворота на 90 градусов по часовой стрелке:")
    print(matrix)

    # поворот на 90 градусов против часовой стрелки
    rotate_counterclockwise(matrix, n)
    print("\nПосле поворота на 90 градусов против часовой стрелки:")
    print(matrix)


if __name__ == "__main__":
    main()
