"""Замена всех заглавных согласных английских букв на строчные (Вариант 3)"""

from typing import List

alp: frozenset = {'Z', 'P', 'V', 'X', 'M', 'J', 'W', 'H', 'D', 'T', 'R', 'F', 'C', 'S', 'G', 'B', 'L', 'Q', 'N', 'K'}
# lst: List[str] = input("Введите элементы списка через пробел: ").split()

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
        for i in range(len(lst)):
            for b in lst[i]:  # b - bukva, lst[i] - slovo
                if b in alp:  # alp - alfavit
                    lst[i] = lst[i].replace(b, b.lower())

    print(f"Измененный список: {lst}")

"""Из одномерного массива удаить все элементы в составе которых есть 6, алго за 1 цикл"""