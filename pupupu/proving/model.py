import timeit
import matplotlib.pyplot as plt

# Параметры эксперимента
list_sizes = [10**5, 10**6, 10**8]  # Размеры списков
index = -1  # Индекс для доступа (в конце списка)
value = 0  # Значение, которое будет искаться для index (в начале списка)

# Функции для тестирования
def get_element_by_index(a, index):
    return a[index]

def get_index_of_element(a, value):
    return a.index(value)

# Замеры времени
index_times = []
search_times = []

for size in list_sizes:
    a = list(range(size))

    # Время выполнения доступа по индексу
    index_time = timeit.timeit(lambda: get_element_by_index(a, index), number=1000)
    index_times.append(index_time)

    # Время выполнения поиска по значению
    search_time = timeit.timeit(lambda: get_index_of_element(a, value), number=1000)
    search_times.append(search_time)

# Визуализация результатов
plt.figure(figsize=(10, 5))
plt.plot(list_sizes, index_times, label='Доступ по индексу a[i]', marker='o')
plt.plot(list_sizes, search_times, label='Поиск индекса элемента a.index(value)', marker='o')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.title('Сложность операций над list')
plt.grid()
plt.show()
