import timeit
import seaborn as sns
import matplotlib.pyplot as plt

from random import randint

sns.set_style("whitegrid")


def get_element_by_index(a, index):
    return a[index]


a = list(range(10**8))
# b = list(range(10**10))
times = []
# times_b = []
idxs = []


for i in range(1000):
    idx = randint(0, 10**8-1)
    # idx_b = randint(0, 10**10-1)
    idx_time = timeit.timeit(lambda: get_element_by_index(a, idx))
    # idx_time_b = timeit.timeit(lambda: get_element_by_index(b, idx_b))
    print(f"{idx:^10} | {idx_time:4f}")
    # print(f"{idx:^10} | {idx_time:4f} |       {idx_b:^10} | {idx_time_b:4f}")

    idxs.append(idx)
    # idxs.append(idx_b)
    times.append(idx_time)
    # times_b.append(idx_time_b)


plt.figure(figsize=(12, 6))
sns.scatterplot(x=idxs, y=times, label='Доступ по индексу list[i]')
# sns.scatterplot(x=idxs, y=times_b, label='Доступ по индексу list_b[i]', color="red", marker='o')
plt.xlabel('Индекс')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сложность доступа по индексу (O(1))')
plt.legend()
plt.show()
