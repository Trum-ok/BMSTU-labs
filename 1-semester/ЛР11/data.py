import random


def random_list(n: int) -> list[int]:
    """
    `list` рандомных чисел от 0 до 100 длинной `n`
    """
    return [random.randint(0, 100) for _ in range(n)]


def reversed_list(arr: list[int]) -> list[int]:
    """
    перевернутый `arr`
    """
    return arr[::-1]


def sorted_list(n: int) -> list[int]:
    """
    упорядоченный (возростание) `list` длинной `n`
    """
    return list(range(1, n + 1))


if __name__ == "__main__":
    r = random_list(5)
    print(f"рандомный: {r}")
    print(f"перевернутый: {reversed_list(r)}")
    print(f"отсортированный: {sorted_list(5)}")
