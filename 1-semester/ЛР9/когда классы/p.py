from math import isqrt
from utils import print_matrix


def count_squares(row: list[int]) -> int:
    """Подсчитывает количество полных квадратов в строке матрицы"""
    return sum(1 for x in row if isqrt(x) ** 2 == x)


def main(a: list[int], b: list[int]) -> tuple[list[list[int]], list[int]]:
    la = len(a)
    lb = len(b)
    M = [[a[i] * b[j] for j in range(lb)] for i in range(la)]
    s = [count_squares(row) for row in M]
    return M, s


if __name__ == '__main__':
    print('Элементы массивов вводятся через пробел')

    a = input('Введите элементы массива A: ')
    b = input('Введите элементы массива B: ')

    a = [int(n) for n in a.split()]
    b = [int(n) for n in b.split()]

    M, s = main(a, b)
    print("Матрица M и столбец S:")
    print_matrix(M, side_info=s)
