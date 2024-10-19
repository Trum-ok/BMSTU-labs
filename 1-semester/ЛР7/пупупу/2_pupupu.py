
print(" ".join([f"{i} {i*2}" if i % 3 == 0 else str(i) for i in [int(i) for i in input("Введите элементы списка через пробел: ").split()]]))
