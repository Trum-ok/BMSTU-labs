lst = [int(x) for x in input("Введите элементы списка через пробел: ").split()]

if len(lst) == 0:
    print("Список пуст!")
elif len(lst) == 1:
    if lst[0] % 2 == 0:
        print(1)
    else:
        print(0)
else:
    max_len = 0
    current_len = 0

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            if i > 0 and lst[i] < lst[i - 1] and lst[i - 1] % 2 == 0:  # убывающая и предыдущий чётный
                current_len += 1
            else:
                current_len = 1  # начинаем новую послед с текущего чётного
        else:
            current_len = 0  # сброс длины если элемент нечётный

        if current_len > max_len:
            max_len = current_len

    print("Максимальная длина:", max_len)
