from collections import defaultdict


def main(lst: list) -> int:
    counter = defaultdict(int)
    for i in lst:
        if i in counter:
            return i
        else:
            counter[i] += 1

    raise ValueError("В списке нет повторяющихся элементов!")


if __name__ == "__main__":
    lst = [int(x) for x in input().split()]
    print(main(lst))
