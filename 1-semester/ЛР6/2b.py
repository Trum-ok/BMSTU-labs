lst = [float(x) for x in input("Введите элементы списка через пробел: ").split()]
index = int(input("Введите индекс для удаления элемента: "))

if index < 0:
    print("Разрешены только положительные индексы")
else:
    if index < len(lst):
        for i in range(index, len(lst) - 1):
            lst[i] = lst[i + 1]  # сдвиг элементов влево
        lst = lst[:-1]

        print("Изменённый список:", lst)
    else:
        print("Такого элемента нет в списке")
