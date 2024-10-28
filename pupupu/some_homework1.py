def main(lst: list) -> int:
    for i in range(len(lst)):
        index = abs(lst[i]) - 1
        if lst[index] < 0:  # если значение по индексу отрицательное, то элемент повторяется
            return abs(lst[i])
        lst[index] = -lst[index]  # помечаем элемент как посещённый
    return -1


if __name__ == "__main__":
    lst = [int(x) for x in input().split()]
    print(main(lst))
