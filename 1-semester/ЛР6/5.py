lst = [int(x) for x in input("Введите элементы списка через пробел: ").split()]

if len(lst) == 0:
    print("Список пуст!")
elif len(lst) == 1:
    print("Нечего менять местами!")
else:
    min_index = max_index = 0

    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
        if lst[i] > lst[max_index]:
            max_index = i

        lst[min_index], lst[max_index] = lst[max_index], lst[min_index]  # переприсваивание

    print("Изменённый список:", lst)
