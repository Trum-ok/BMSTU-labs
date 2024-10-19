alp: frozenset = {'Z', 'P', 'V', 'X', 'M', 'J', 'W', 'H', 'D', 'T', 'R', 'F', 'C', 'S', 'G', 'B', 'L', 'Q', 'N', 'K'}
lst = input("Введите элементы списка через пробел: ").split()

for i in range(len(lst)):
    for b in lst[i]:
        if b in alp:
            lst[i] = lst[i].replace(b, b.lower())

print(lst)
