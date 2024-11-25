def partition(arr: list[int], l: int, h: int) -> int:
    """Функция для разделения массива с выбором опорного элемента"""
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quick_iterative(arr: list[int], l, h):
    """
    Очень quick сортировка
    """
    size = h - l + 1
    stack = [0] * size

    top = 0
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h)

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


if __name__ == "__main__":
    # arr = [4, 3, 5, 2, 1, 3, 2, 3]
    arr = list(range(1000000))
    n = len(arr)
    quick_iterative(arr, 0, n-1)
    print (f"Sorted array: {arr}")
