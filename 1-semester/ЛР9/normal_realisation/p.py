"""
Даны два одномерных целочисленных массива A и B. Сформировать матрицу
M, такую что m[i][j] =a[i]*b[j].
Определить количество полных квадратов в каждой строке матрицы.
Записать значения в массив S.
Напечатать матрицу M в виде матрицы и рядом столбец S.
"""

from matrix_anot import Matrix
from math import isqrt


def count_squares(row: list[int]) -> int:
    """Функция для подсчета полных квадратов в целочисленном списке"""
    cnt = 0
    for x in row:
        if isqrt(x) ** 2 == x:
            cnt += 1
    return cnt


def main(a: list[int], b: list[int]) -> Matrix:
    la = len(a)
    lb = len(b)
    M = Matrix([[0] * lb for _ in range(la)])
    s: list[int] = []

    for i in range(la):
        for j in range(lb):
            M[i][j] = a[i] * b[j]
        s.append(count_squares(M[i]))

    M.side_info = s
    return M


if __name__ == '__main__':
    print('Элементы массивов вводятся через пробел')
    a = [int(n) for n in input('Введите элементы массива A: ').split(" ")]
    b = [int(n) for n in input('Введите элементы массива B: ').split(" ")]

    M = main(a, b)
    print(M)
