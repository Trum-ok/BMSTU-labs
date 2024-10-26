"""После каждого элемента целочисленного списка, кратного трём, добавить его удвоенное значение (Вариант 1)"""

from typing import List, Optional

lst: List[Optional[int]] = [int(i) for i in input("Введите элементы списка через пробел: ").split()]
t_cnt = sum(bool(abs(i) % 3 == 0) for i in lst)
lst += [None]*t_cnt

# lst.extend([None]*t_cnt)

i = len(lst) - t_cnt - 1

while i >= 0:
    if abs(lst[i]) % 3 == 0:
        lst[i + t_cnt] = lst[i] * 2
        t_cnt -= 1
        lst[i + t_cnt] = lst[i]
    else:
        lst[i + t_cnt] = lst[i]
    i -= 1

print(f"Измененный список: {lst}")
