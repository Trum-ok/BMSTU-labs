from utils import print_matrix


def middle_slice(array: list[list[list[int]]]) -> list[list[int]]:
    """Возвращает срез трехмерного массива по его максимальной размерности."""
    x_len, y_len, z_len = len(array), len(array[0]), len(array[0][0])

    # определяем максимальное измерение и находим индекс середины
    max_dimension = max(x_len, y_len, z_len)

    if max_dimension == x_len:
        middle_index = x_len // 2
        return array[middle_index]
    elif max_dimension == y_len:
        middle_index = y_len // 2
        return [matrix[middle_index] for matrix in array]
    else:
        middle_index = z_len // 2
        return [[row[middle_index] for row in matrix] for matrix in array]


def main() -> None:
    x, y, z = map(int, input("Введите размеры X, Y, Z через пробел: ").split())
    array = []

    print("Введите элементы массива построчно (размером X * Y * Z):")
    for i in range(x):
        matrix = []
        for j in range(y):
            row = list(map(int, input().split()))
            if len(row) != z:
                print(f"Ошибка: каждая строка должна содержать ровно {z} элементов.")
                return
            matrix.append(row)
        array.append(matrix)

    print("\nИсходный массив:")
    for matrix in array:
        print_matrix(matrix)

    result = middle_slice(array)
    print("\nСрез массива по максимальному измерению:")
    print_matrix(result)


if __name__ == "__main__":
    main()
