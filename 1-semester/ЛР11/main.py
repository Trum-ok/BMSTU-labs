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


def process(n: int) -> tuple[str, str, str]:
    arr_random = random_list(n)
    arr_sorted = sorted_list(n)
    arr_reversed = reversed_list(arr_sorted)

    return (
        measure_time_and_swaps(arr_sorted),
        measure_time_and_swaps(arr_random),
        measure_time_and_swaps(arr_reversed),
    )


def measure_time_and_swaps(arr: list[int]) -> str:
    start_time = time.time()
    _, swaps = quick(arr)
    end_time = time.time()
    time_taken = round(end_time - start_time, 6)
    return f"{time_taken} сек\n{swaps} перестановок"


def compare(*args: int) -> str:
    results = [process(n) for n in args]
    headers = [""] + list(args)
    rows = [
        ["Упорядоченный список"] + [result[0] for result in results],
        ["Случайный список"] + [result[1] for result in results],
        ["Упорядоченный в обратном порядке"] + [result[2] for result in results],
    ]
    return tabulate(rows, headers=headers, tablefmt="grid")


if __name__ == "__main__":
    main()
