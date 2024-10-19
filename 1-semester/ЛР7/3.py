alp: frozenset = {'c', 'l', 't', 'r', 'z', 'd', 'n', 'x', 'h', 'm', 's', 'g', 'v', 'q', 'j', 'w', 'k', 'p', 'f', 'b'}
lst = input("Введите элементы списка через пробел: ").split()

ocnt = 0
cnt = 0
idx: int

for i in range(len(lst)):
    for b in lst[i]:
        if b in alp:
            cnt += 1
    if cnt > ocnt:
        idx = i
    ocnt = cnt
    cnt = 0

print(lst[idx])
