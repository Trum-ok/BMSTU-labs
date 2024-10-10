"""
Лабораторная работа №5 'График'
Артамонов Аркадий ИУ7-16Б (Вариант 40)

Программа для:
    - Вычисление и вывод значений функции W(t)
    - Построение графика зависимости W от t
"""

from decimal import Decimal, getcontext
getcontext().prec = 6

# t0 = Decimal(-0.5)
# step = Decimal(0.05)
# tn = Decimal(0.5)
t0 = Decimal(float(input("Введите начальное значение t0: ")))
step = Decimal(float(input("Введите шаг: ")))
tn = Decimal(float(input("Введите конечное значение tn: ")))

# characters = 80
characters = int(input("Введите ширину графика: "))
eps = 2e-1 - 0.15

w_min = 10 * 10
w_max = 1e-10
t_min = None

iters = int((tn - t0) / step) + 1

print('+' + '-' * 30 + "+",
      '|      t     |        W        |',
      '|------------+-----------------|', sep='\n')

# значения W(t) для каждого шага
for i in range(iters):
    W = (2048 * t0**12) - (6144 * t0**10) + (6912 * t0**8) - (3584 * t0**6) + (840 * t0**4) - (72 * t0**2) + 1
    if t0 < 1e-17 and t0 > -1e-17:
        t0 = Decimal(0.0)
    if W < w_min:
        w_min = W
        t_min = t0
    if W > w_max:
        w_max = W
    print(f'| {t0:^10.2g} | {W:^15.4g} |')
    t0 += step

print("+" + '-' * 30 + "+")
print("\n\n",
      f"w_min = {w_min} | t_min = {t_min}", end= ""
      )


# мин и макс значеня для OW (Oy)
ymin, ymax = w_min, w_max  # ~ диапазон значений функции
xmin, xmax = Decimal(-0.5), tn
division_price = abs(xmin - xmax) / characters

print("\n")
ticks_y = int(input("Введите количество засечек для оси W (от 4 до 8): "))
print("\n")

# Шаг и засечки для оси W
y_step = (ymax - ymin) / (ticks_y - 1)

print("{:>10}{}".format("Ось W", " ^"))
for i in range(ticks_y - 1, -1, -1):
    y = ymin + i * y_step
    current_column = 1

    print(f'{y:>10.2g} |', end='')  # значения OW

    # пересчет W(t) для каждой итерации (МЫ ЖЕ НЕ МОЖЕМ СЛОВАРЬ ИСПОЛЬЗОВАТЬ)
    t0 = Decimal(-0.5)
    for j in range(iters):
        W = (2048 * t0**12) - (6144 * t0**10) + (6912 * t0**8) - (3584 * t0**6) + (840 * t0**4) - (72 * t0**2) + 1
        if t0 < 1e-17 and t0 > -1e-17:
            t0 = Decimal(0.0)
        normalized_t = t0 + Decimal(0.5)  # нормализация по Оt
        posx_absolute = (normalized_t // division_price) + 1
        posx = posx_absolute - current_column + 1

        if t0 != 0 and (abs(W - y) <= eps):
            print("{:>{}}".format('*', posx + 1), end='')
            current_column += posx + 1
        elif t0 == 0:
            print("{:>{}}".format('|', posx), end='')
            current_column += posx

        t0 += step

    print()

# Оx
print(' ' * 11 + '+' + '-' * characters + '-->  Ось t')
print(' ' * 11, end='')

x_step = (tn - Decimal(-0.5)) / (iters - 1)
x_count = iters // 2 + 1

l_count = x_count // 2
r_count = x_count // 2 + (1 if iters % 2 != 0 else 0)

symb = l_count * 5 + r_count * 4
c = (symb // (x_count - 1)) + 1

# for i in range(iters):
#     if i % 2 == 0:
#         t = Decimal(-0.5) + i * x_step
#         posx = round((t - Decimal(-0.5)) / (Decimal(0.5) - Decimal(-0.5)) * (characters - 1))
#         print(f'{t:^5.2g}', end=' ' * c)

#         if i < iters - 1:  # лишний пробел в конце
#             print(' ' * (characters // iters - len(f'{t:^5.2g}')), end='')

# print()

for i in range(iters):
    if i % 2 == 0:
        t = Decimal(-0.5) + i * x_step
        label = f'{t:^5.1g}'

        total_width = characters // iters
        padding = total_width - len(label)

        print(f"{label}{' '*(characters//(iters+2))}", end="")

print()
