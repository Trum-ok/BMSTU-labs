f, p = map(int, input().split())

back = 0
m5 = f

# m1 = ...

# m2 = ...

# m3 = m2*p + back2
# mi % p -  сдача, которая должна быть с предыдущего дня

print("_"*10)
n4 = m5 // p  # сколько бутылок сдали в 4 день
s4 = (m5 % p)
m4 = (n4 * p) + s4
print(f"ПТ надо денег: {m4}, сдачи с 3 дня: {s4}, бутылок сдать: {n4}")

print("_"*10)
s3 = (m4 % p)
n3 = m4 // p
m3 = (n3 * f) + s3
print(f"ЧТ надо денег: {m3}, сдачи с 2 дня: {s3}, бутылок сдать: {n3}")

print("_"*10)
s2 = (m3 % p)
n2 = m3 // p
m2 = (n2 * f) + s2
print(f"СР надо денег: {m2}, сдачи с 1 дня: {s2}, бутылок сдать: {n2}")

print("_"*10)
s1 = (m2 % p)
n1 = m2 // p
m1 = (n1 * f) + s1
print(f"ВТ надо денег: {m1}, сдачи с 1 дня: {s1}, бутылок сдать: {n1}")

print("_"*10)
s0 = (m1 % p)
n0 = m1 // p
m0 = (n0 * f) + s0
print(f"ПН надо денег: {m0}, сдачи с 1 дня: {s0}, бутылок сдать: {n0}")


# s = m1 + m2 + m3 + m4 + m5
# print(m2)
