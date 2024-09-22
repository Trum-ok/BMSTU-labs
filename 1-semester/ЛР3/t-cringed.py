"""
Лабораторная работа №3 'Треугольник'
Артамонов Аркадий ИУ7-16Б

Программа для:
    - Вычисления длин сторон треугольника
    - Вычисления биссектрисы наименьшего угла
    - Определения принадлежности точки к треугольнику и расстояния до стороны
"""

import math

# Ввод координат вершин треугольника
x1, y1 = map(float, input("Введите координаты первой точки (через пробел): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (через пробел): ").split())
x3, y3 = map(float, input("Введите координаты третьей точки (через пробел): ").split())

if any(coord < 0 for coord in [x1, x2, x3, y1, y2, y3]):
    print("Введены некорректные (отрицательные) координаты.")
    exit(-1)

# Вычисление длин сторон треугольника
side_a = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
side_b = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
side_c = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if any(side == 0 for side in [side_a, side_b, side_c]):
    print('Это отрезок.')
    exit(-1)

print(f"Длины сторон треугольника: a = {side_a:5g}, b = {side_b:5g}, c = {side_c:5g}")

# Проверка, является ли треугольник прямоугольным
sides = sorted([side_a, side_b, side_c])
if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
    print("Треугольник прямоугольный.")
else:
    print("Треугольник не является прямоугольным.")

# Вычисление биссектрисы, проведенной из наименьшего угла
cos_A = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
cos_B = (side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)
cos_C = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)

# Определение наименьшего угла
if cos_A <= cos_B and cos_A <= cos_C:
    # Наименьший угол A, биссектриса будет для стороны a
    bisector = math.sqrt(side_b * side_c * ((side_b + side_c + side_a) * (side_b + side_c - side_a))) / (side_b + side_c)
    print(f"Длина биссектрисы из наименьшего угла (A): {bisector:.5g}")
elif cos_B <= cos_A and cos_B <= cos_C:
    # Наименьший угол B, биссектриса будет для стороны b
    bisector = math.sqrt(side_a * side_c * ((side_a + side_c + side_b) * (side_a + side_c - side_b))) / (side_a + side_c)
    print(f"Длина биссектрисы из наименьшего угла (B): {bisector:.5g}")
else:
    # Наименьший угол C, биссектриса будет для стороны c
    bisector = math.sqrt(side_a * side_b * ((side_a + side_b + side_c) * (side_a + side_b - side_c))) / (side_a + side_b)
    print(f"Длина биссектрисы из наименьшего угла (C): {bisector:.5g}")

# Ввод координат точки
x, y = map(float, input("Введите координаты точки (через пробел): ").split())

# Проверка, находится ли точка внутри треугольника
d1 = (x - x3) * (y2 - y3) - (x2 - x3) * (y - y3)
d2 = (x - x1) * (y3 - y1) - (x3 - x1) * (y - y1)
d3 = (x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)

has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

if not (has_neg and has_pos):
    print("Точка находится внутри треугольника.")

    # Вычисление расстояния до ближайшей стороны
    d_to_side1 = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / side_c
    d_to_side2 = abs((y3 - y2) * x - (x3 - x2) * y + x3 * y2 - y3 * x2) / side_a
    d_to_side3 = abs((y1 - y3) * x - (x1 - x3) * y + x1 * y3 - y1 * x3) / side_b

    nearest_distance = min(d_to_side1, d_to_side2, d_to_side3)
    print(f"Расстояние до ближайшей стороны треугольника: {nearest_distance:5g}")
else:
    print("Точка находится вне треугольника.")
