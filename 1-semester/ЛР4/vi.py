# Автор: Овсянникова Виктория
# Группа: ИУ7-16Б 56 вариант
# Назначение программы: вычисление суммы ряда с точностью до члена eps

from math import *

# ввод данных
x = float(input("Введите x: "))
eps = float(input("Введите eps: "))
step = int(input("Введите шаг вывода: "))
maxit = int(input("Введите максимальное количество итераций: "))

term = 1  # 1-ый член ряда
sums = term  # сумма ряда
n = 1
it = 1
last = 1


print("-" * 42)
print(f"| {'№ итерации':^10} | {'x':^10} | {'sum(y)':^10} |")
print("-" * 42)
print(f"| {it:<10} | {term:^10.5g} | {sums:^10.5g} |")
print("-" * 42)

while abs(term) > eps and (it < maxit):
    last *= x
    term = last / n
    sums += term
    n += 1
    it += 1

    if (step <= 0) or (maxit <= 0):  # вызод из цикла в случае невалидного ввода
        print('Ошибка')
        break
    else:
        if (it % step == 1) or (step == 1) :  # каждые n шагов вывода
            print(f"| {it:<10} | {term:^10.5g} | {sums:^10.5g} |")
    print("-" * 42)

# вывод результата
if (abs(term) > eps) and (maxit <= it):  # если не удалось высчитать сумму за указанные параметры
    print(f'За указанное число итераций ({maxit}) необходимой точности достичь не удалось.')
elif abs(term) <= eps:
    print(f"Сумма бесконечного ряда - {sums:.5g}, вычислена за {it} итераций.")
    print("-" * 42)
