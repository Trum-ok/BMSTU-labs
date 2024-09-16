"""
Лабораторная работа №1 'Параметры объемного тела'
Артамонов Аркадий ИУ7-16Б (10 вариант)

Программа для вычисления:
    - объема шарового сектора
    - площади шарового сектора
    - площади поверхности конуса
"""

# 0. Импорт необходимых модулей и ввод данных
from math import sqrt, pi

sphere_r = float(input('Введите радиус шара: '))  # R сферы
cone_h = float(input('Введите высоту конуса: '))  # h конуса

# 1. Вычисление параметров конуса
cone_r = sqrt(cone_h * (2 * sphere_r - cone_h))  # R основания конуса
cone_l = sqrt(sphere_r ** 2 + cone_h ** 2)  # образующая конуса

# 2. Вычисление объемов (V)
sphere_v = 4/3 * pi * sphere_r ** 3  # V шара
small_segment_v = pi * cone_h ** 2 * (3 * sphere_r - cone_h) / 3  # V малой отсеченной части шара
big_segment_v = sphere_v - small_segment_v  # V большой отсеченной части шара
cone_v = 1/3 * cone_r * cone_h  # V конуса
sector_v = big_segment_v + cone_v  # V сектора

# 3. Вычисление площадей (S)
sphere_s = 4 * pi * sphere_r ** 2  # S поверхности шара
small_segment_s = 4 * pi * sphere_r * cone_h  # S малой отсеченной части шара
big_segment_s = sphere_s - small_segment_s  # S большой отсеченной части шара
cone_s = pi * cone_r * cone_l + pi * cone_r ** 2  # S поверхности конуса
sphere_sector_s = big_segment_s + cone_s  # S сектора


# 4. Вывод вычесленных значений
print(f"Объем шарового сектора: {round(sector_v, 5)}")
print(f"Площадь шарового сектора: {round(sphere_sector_s, 5)}")
print(f"Площадь поверхности конуса: {round(cone_s, 5)}")
