"""Поиск элемента с наибольшим числом английских согласных букв (Вариант 2)"""

from typing import List

alp: frozenset = {'c', 'l', 't', 'r', 'z', 'd', 'n', 'x', 'h', 'm', 's', 'g', 'v', 'q', 'j', 'w', 'k', 'p', 'f', 'b'}
# lst: List[str] = input("Введите элементы списка через |: ").split('|')

lst: List[str] = []
n = int(input("Введите количество элементов списка: "))
if n <= 0:  # тест на iq
    print("Количество элементов в списке должно быть больше 0")
else:
    for j in range(n):
        lst.append(input(f"Введите {j + 1} элемент списка: "))

    if len(lst) == 0:
        print("Список пуст, искать нечего")
    else:
        old_cnt = 0  # старый счетчит
        cnt = 0  # новый счетчик
        idx = 0  # индекс элемента

        for i in range(len(lst)):
            for b in lst[i].lower():  # b - bukva, lst[i] - slovo
                if b in alp:  # alp - alfavit
                    cnt += 1  # увеличиваем счетчик, если буква в алфавите (из согласных)
            if cnt > old_cnt:
                idx = i
                old_cnt = cnt
            cnt = 0

    if old_cnt == 0:
        print("В списке нет элементов с согласными буквами")
    else:
        print(f"Искомый элемент: {lst[idx]}")
