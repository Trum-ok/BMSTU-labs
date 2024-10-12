# """
# Лабораторная работа №4 'Сумма бесконечного ряда'
# Артамонов Аркадий ИУ7-16Б (44 Вариант)

# Программа для вычисления суммы бесконечного ряда:
# y = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)! +- ε
# """


# def main(x: float, epsilon: float, its: int, step: int) -> float:
#     term = x  # Начальный член ряда (x^(2*0+1) / (2*0+1)! = x)
#     sum_series = term  # Сумма ряда
#     n = 2  # Счетчик нечётных степеней (2n+1)
#     iteration = 1

#      # Заголовок таблицы
#     print("-" * 39)
#     print(f"| {'№ итерации':^10} | {'t':^10} | {'s':^10} |")
#     print("-" * 39)
#     print(f"| {iteration:<10} | {term:^10.5g} | {sum_series:^10.5g} |")

#     # Итерационный процесс
#     while (abs(term) > epsilon) and (iteration < its):
#         # term *= x**2 / ((2 * n) * (2 * n + 1))  # Вычисление следующего члена ряда
#         # n += 2
#         term = x/n
#         sum_series += term  # Добавление члена к сумме
#         n += 2
#         iteration += 1

#         # Вывод каждой итерации
#         print(f"| {iteration:<10} | {term:^10.5g} | {sum_series:^10.5g} | {1/(n-2)}")

#     # Конец таблицы
#     print("-" * 39)

#     # Возвращаем итоговую сумму и количество итераций
#     return sum_series, iteration


# if __name__ == "__main__":
#     x = float(input("Введите значение x: "))
#     epsilon = float(input("Введите значение ε: "))
#     its = int(input("Введите количество итераций: "))
#     step = int(input("Введи шаг вывода: "))
#     result, iterations = main(x, epsilon, its, step)
#     print(f"Сумма бесконечного ряда - {result:.5g}, вычислена за {iterations} итераций.")


# Ввод с клавиатуры
x = float(input("Введите значение x: "))
epsilon = float(input("Введите значение epsilon: "))

sum_series = 0.0
n = 1
term = (-x**(2*n+1))  # Начальное значение числителя для n = 1
fact = 1  # Начальный факториал для 2n (2*1)

while abs(term / fact) > epsilon:
    sum_series += (-1)**n * (term / fact)
    
    n += 1
    
    # Обновляем числитель и факториал для следующего шага
    term *= -x**2  # Обновляем степень x
    fact *= (2*n - 1) * (2*n)  # Обновляем факториал для следующего члена

print(f'Сумма ряда: {sum_series}')