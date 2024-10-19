lst = [int(i) for i in input("Введите элементы списка через пробел: ").split()]
t_cnt = sum(bool(i % 3 == 0) for i in lst)

lst.extend([None]*t_cnt)

i = len(lst) - t_cnt - 1
while i >= 0:
    if lst[i] % 3 == 0:
        lst[i + t_cnt] = lst[i] * 2
        t_cnt -= 1
        lst[i + t_cnt] = lst[i]
    else:
        lst[i + t_cnt] = lst[i]
    i -= 1

print(lst)
