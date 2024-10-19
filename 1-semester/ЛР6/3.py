lst = [float(x) for x in input("Введите элементы списка через пробел: ").split()]

if len(lst) == 0:
    print("Список пуст!")
elif len(lst) == 1:
    print(f"В списке всего один элемент ({lst[0]}). Экстремумов нет.")
elif len(lst) == 2:
    print(f"В списке два элемента ({lst}). Экстремумов нет, т.к. требуется минимум три элемента.")
else:
    k = int(input("Введите номер экстремума K: "))
    if k <= 0:
        print("Введите корректный номер экстремума (>0)")
    else:

        found_extremum = None
        extremum_count = 0

        # поиск
        for i in range(1, len(lst) - 1):
            if (lst[i] > lst[i - 1] and lst[i] > lst[i + 1]) or (lst[i] < lst[i - 1] and lst[i] < lst[i + 1]):
                extremum_count += 1
                if extremum_count == k:  # к-й экстремум
                    found_extremum = lst[i]
                    break

        # проверка
        if extremum_count == 0:
            print("Экстремумов в списке нет.")
        elif k <= 0:
            print("Номер экстремума должен быть положительным числом.")
        elif found_extremum is not None:
            print(f"{k}-й экстремум: {found_extremum}")
        else:
            print(f"Недостаточно экстремумов, найдено только {extremum_count}.")
