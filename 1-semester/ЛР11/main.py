import time
from tabulate import tabulate

from quick_sort import quick
from data import random_list, reversed_list, sorted_list


def main() -> None:
    try:
        a = list(map(int, input("Введите элементы списка через пробел: ").split()))
        if not a:
            raise ValueError("Список не должен быть пустым.")
        print(f"Исходный список: {a}")

        a_sorted, cnt = quick(a)
        print(f"Отсортированный список: {a_sorted} за {cnt} перестановок\n")

        n_values = input("Введите размеры N1 N2 N3 через пробел: ").split()
        if len(n_values) != 3:
            raise ValueError("Необходимо ввести ровно три значения.")

        n1, n2, n3 = map(int, n_values)
        table = compare(n1, n2, n3)
        print("Результаты сортировки:")
        print(table)

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


def process(n: int) -> tuple[tuple[float, int], tuple[float, int], tuple[float, int]]:
    arr_random = random_list(n)
    arr_sorted = sorted_list(n)
    arr_reversed = reversed_list(arr_sorted)

    return (
        measure_time_and_swaps(arr_random),
        measure_time_and_swaps(arr_sorted),
        measure_time_and_swaps(arr_reversed),
    )


def measure_time_and_swaps(arr: list[int]) -> tuple[float, int]:
    start_time = time.time()
    _, swaps = quick(arr)
    end_time = time.time()
    return round(end_time - start_time, 6), swaps


def compare(*args: int) -> str:
    results = [process(n) for n in args]
    headers = [""] + list(args)
    rows = [
        ["Упорядоченный список"] + list(map(format_results, results[0])),
        ["Случайный список"] + list(map(format_results, results[1])),
        ["Упорядоченный в обратном порядке"] + list(map(format_results, results[2])),
    ]
    return tabulate(rows, headers=headers, tablefmt="grid")


def format_results(result: tuple[float, int]) -> str:
    return f"{result[0]} сек\n{result[1]} перестановок"


if __name__ == "__main__":
    main()
