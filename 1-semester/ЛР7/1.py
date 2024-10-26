"""Удалить все нулевые элементы целочисленного списка (Вариант 1)"""

from typing import List

lst: List[int] = list(map(int, input("Введите элементы списка через пробел: ").split()))

if len(lst) == 0:
    print("Список пуст, изменять нечего")
else:
    idx = 0 # индексы подходящих элементов
    i = 0
    while i < len(lst):
        if lst[i] != 0:
            lst[idx] = lst[i]
            idx += 1
        i += 1

    print(f"Измененный список: {lst[:idx]}")

    # for i in range(idx):
    #     print(lst[i])

# print(*[int(i) for i in input("Введите элементы списка через пробел: ").split() if int(i) != 0])

#____

# lst: List[int] = list(map(int, input("Введите элементы списка через пробел: ").split()))
# updated_lst = [i for i in lst if i != 0]

# print(*updated_lst)
