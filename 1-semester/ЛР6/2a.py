lst = [float(x) for x in input("Введите элементы списка через пробел: ").split()]

if len(lst) == 0:
    print("Список пуст, удалять нечего")
else:
    index = int(input("Введите индекс для удаления элемента: "))
    if -len(lst) <= index < len(lst):
        del lst[index]  # удаление элемента по индексу
        print("Изменённый список:", lst)
    else:
        print("Такого элемента нет в списке")
