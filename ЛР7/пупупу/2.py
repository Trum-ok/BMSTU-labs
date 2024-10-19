lst = [int(i) for i in input("Введите элементы списка через пробел: ").split()]

for i in lst:
    if i % 3 == 0:
        print(i, i*2, end=" ")
    else:
        print(i, end=" ")
print("\n")

