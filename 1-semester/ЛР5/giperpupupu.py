"""
Лабораторная работа №5 'График'
Артамонов Аркадий ИУ7-16Б (Вариант 40)

Программа для:
    - Вычисления и вывода значений функции W(t)
    - Построения графика зависимости W от t
"""

# Ввод данных
tz = float(input("Введите начальное значение t0: "))
step = float(input("Введите шаг: "))
tn = float(input("Введите конечное значение tn: "))
characters = int(input("Введите ширину графика: "))

# tz = -0.5
# step = 0.05
# tn = 0.5
# characters = 100

flag = (step <= 0) or (characters < 80) or (characters >= 180) or (tz >= tn)
if flag:
    raise ValueError("Введите адекватные значения, пожалуйста")

t0 = tz

sc = 11
if tz < -1e4 or tn > 1e4:
    sc = 16

# Инициализация переменных для вычисления минимума и максимума функции
w_min = float('inf')
w_max = float('-inf')
iters = int((tn - t0) / step) + 1

# Вывод таблицы значений функции
print('+' + '-' * 30 + "+",
      '|      t     |        W        |',
      '|------------+-----------------|', sep='\n')

for i in range(iters):
    W = (2048 * t0**12) - (6144 * t0**10) + (6912 * t0**8) - (3584 * t0**6) + (840 * t0**4) - (72 * t0**2) + 1  # noqa: E501
    if abs(t0) < 1e-3:
        t0 = 0.0
    if W < w_min:
        w_min = W
    if W > w_max:
        w_max = W
    print(f'| {t0:^10.2g} | {W:^15.4g} |')
    t0 += step

print("+" + '-' * 30 + "+")
# Определение диапазонов осей

ymin, ymax = tz, tn  # Диапазон значений функции

# Масштабирование и вычисление стоимости одного знакоместа по оси W
division_price = abs(w_min - w_max) / characters

# Ввод количества засечек для оси t
print("\n")
ticks_w = int(input("Введите количество засечек для оси W (от 4 до 8): "))
print("\n")

if not (4 <= ticks_w <= 8):
    raise ValueError("количество засечек от 4 до 8")

# Шаг и засечки для оси W
w_step = (w_max - w_min) / (ticks_w - 1)

print(' ' * (sc+1), end='')
for i in range(ticks_w):
    cur_column = 1
    w = w_min + i * w_step

    total_width = (characters // ticks_w)

    if w < 0:
        label = f'{w:<5.1g}'
        padding = total_width - len(label)
        print(f"{label}{" "* padding}", end="")
    else:
        label = f'{w:>5.1g}'
        padding = total_width - len(label)
        print(f"{" "* padding}{label}", end="")

print()
print(' ' * (sc+1) + '+' + '-' * characters + '-->  Ось W')

# Вычисление позиций с логарифмом
for i in range(iters):
    t = ymin + i * step
    print(f'{t:>{sc}.2f} |', end='')

    W = (2048 * t**12) - (6144 * t**10) + (6912 * t**8) - (3584 * t**6) + (840 * t**4) - (72 * t**2) + 1

    if w_max - w_min == 0:  # чтобы избежать деления на ноль
        d = 0.5
    else:
        d = w_max - w_min
    normalized_w = (W - w_min) / d

    posw = int(normalized_w * characters)
    posw_zero = int((characters * -w_min) // (w_max - w_min))
    # print(posw_zero)

    if posw <= posw_zero:
        print(f'{"*" : >{posw + 1}}', end='')
        p = abs(posw_zero - posw)
        if p != 0:
            print(f'{"|" : >{p-1}}', end='')
    else:
        if posw_zero == -1:
            posw_zero += 1
        print(f'{"|" : >{posw_zero}}', end='')
        p = abs(posw - posw_zero)
        print(f'{"*" : >{p}}', end='')

    print()

print("{:>{}}{}".format("Ось t", sc, " v"))
