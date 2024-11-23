def main() -> None:
    a = list(map(int, input("Введите элементы списка через пробел: ").split()))
    print(f"Исходный список: {a}")
    if len(a) < 1:
        raise ValueError("Сортировать нечего! Введите список длиной хотя бы 1.")
    else:
        a_sorted, cnt = quick(a)
    print(f"Отсортированный список: {a_sorted} за {cnt} перестановок")

    return


def quick(arr: list[int]) -> tuple[list[int], int]:
    """
    Алгоритм быстрой сортировки с подсчетом перестановок
    """
    swaps = 0
    if len(arr) == 0:
        return [], swaps
    if len(arr) == 1:
        return arr, swaps
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            swaps += 1
        return arr, swaps
    else:
        idx = len(arr)//2-1
        pivot = arr[idx]
        less, greater = [], []
        for num in arr:
            if num < pivot:
                less.append(num)
                swaps += 1
            elif num > pivot:
                greater.append(num)
                swaps += 1

        sorted_less, less_swaps = quick(less)
        sorted_greater, greater_swaps = quick(greater)

        swaps += less_swaps + greater_swaps

        return sorted_less + [pivot] + sorted_greater, swaps


def compare_of_three():
    pass


if __name__ == "__main__":
    # try:
    #     main()
    # except ValueError as e:
    #     print(e)
    # except Exception as e:
    #     print(e)
    main()
