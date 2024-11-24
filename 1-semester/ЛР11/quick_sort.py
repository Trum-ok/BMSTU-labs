def quick(arr: list[int]) -> tuple[list[int], int]:
    """
    Быстрой сортировки с подсчетом перестановок
    ### Args:
    - arr `list[int]`: список, который необходимо отсортировать
    ### Returns:
    - `tuple[list[int], int]`: отсортированный список и количество перестановок
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
        pivot = [arr[idx]]
        less, greater = [], []

        for i in range(len(arr)):
            if arr[i] < pivot[0]:
                less.append(arr[i])
                swaps += 1
            elif arr[i] > pivot[0]:
                greater.append(arr[i])
                swaps += 1
            elif arr[i] == pivot[0] and i != idx:
                pivot.append(arr[i])
                swaps += 1

        sorted_less, less_swaps = quick(less)
        sorted_greater, greater_swaps = quick(greater)

        swaps += less_swaps + greater_swaps
        return sorted_less + pivot + sorted_greater, swaps


if __name__ == "__main__":
    print(quick([1, 4, 2, 0, 1, 3]))
