"""
Даны два одномерных целочисленных массива A и B.
Сформировать матрицу M, такую что m[i][j] = a[i]*b[j].
Определить количество полных квадратов в каждой строке матрицы.
Записать значения в массив S.
Напечатать матрицу M в виде матрицы и рядом столбец S.
"""

from math import isqrt
from utils import print_matrix


def count_squares(row: list[int]) -> int:
    """Подсчитывает количество полных квадратов в строке матрицы"""
    return sum(1 for x in row if isqrt(x) ** 2 == x)


def main(a: list[int], b: list[int]) -> tuple[list[list[int]], list[int]]:
    la = len(a)
    lb = len(b)
    M = [[0] * lb for _ in range(la)]
    s: list[int] = []

    for i in range(la):
        for j in range(lb):
            M[i][j] = a[i] * b[j]
        s.append(count_squares(M[i]))

    return M, s


if __name__ == '__main__':
    try:
        print('Элементы массивов вводятся через пробел')
        a = [int(n) for n in input('Введите элементы массива A: ').split(" ")]
        b = [int(n) for n in input('Введите элементы массива B: ').split(" ")]

        M, s = main(a, b)
        print("Матрица M и столбец S:")
        print_matrix(M, side_info=s)
    except ValueError:
        print('Ошибка ввода! Убедитесь, что все введенные значения — целые числа.')
    except Exception as e:
        print(f"Непредвиденная ошибка: \n{e}")
