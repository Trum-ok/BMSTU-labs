from utils import print_matrix


def is_vowel(char: str) -> bool:
    """Проверяет, является ли символ гласной буквой латинского алфавита (a, e, i, o, u)."""
    vowels = "aeiouAEIOU"
    return char in vowels


def transform_char(char: str) -> str:
    """Преобразует символ: делает согласные заглавными, гласные - строчными."""
    if char.isalpha():
        if is_vowel(char):
            return char.lower()
        else:
            return char.upper()
    return char


def transform_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """Преобразует матрицу, заменяя согласные на заглавные, а гласные на строчные."""
    return [[transform_char(char) for char in row] for row in matrix]


def main() -> None:
    matrix = []
    n, m = map(int, input("Введите размеры матрицы n и m через пробел: ").split())

    print("Введите строки матрицы:")
    for _ in range(n):
        row = list(input())
        if len(row) != m:
            print(f"Ошибка: каждая строка должна содержать ровно {m} символов.")
            return
        matrix.append(row)

    print("Матрица до преобразования:")
    print_matrix(matrix)

    transformed_matrix = transform_matrix(matrix)

    print("Матрица после преобразования:")
    print_matrix(transformed_matrix)


if __name__ == "__main__":
    main()
