lst = [float(x) for x in input("Введите элементы списка через пробел: ").split()]

# мин макс элементы и их индексы
min_value = lst[0]
max_value = lst[0]
min_index = 0
max_index = 0

for i in range(1, len(lst)):
    if lst[i] < min_value:
        min_value = lst[i]
        min_index = i
    if lst[i] > max_value:
        max_value = lst[i]
        max_index = i

lst[min_index], lst[max_index] = lst[max_index], lst[min_index]  # переприсваивание

print("Изменённый список:", lst)
