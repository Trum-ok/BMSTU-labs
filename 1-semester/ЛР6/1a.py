lst = [float(x) for x in input("Введите элементы списка через пробел: ").split()]
index = int(input("Введите индекс для добавления элемента: "))

if (len(lst) == 0 and index != 0) or (index >= len(lst)):
    if index == 0:
        print("В пустой список элемент можно добавить только на нулевую позицию!")
    else:
        print("Индекс превышает длину списка!")
else:
    value = float(input("Введите значение нового элемента: "))
    lst.insert(index, value)  # добавление элемента по индексу

    print("Изменённый список:", lst)
