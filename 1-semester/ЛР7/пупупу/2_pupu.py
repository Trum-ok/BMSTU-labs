lst = [int(i) for i in input("Введите элементы списка через пробел: ").split()]

i:int = 0
n = len(lst)

while i < n:
    if lst[i] % 3 == 0:
        lst.extend([None])
        for j in range(len(lst)-1, i+1, -1):
            lst[j] = lst[j-1]
        lst[i+1] = lst[i] * 2
        i += 2
        n += 1
    else:
        i += 1

print(*lst)
