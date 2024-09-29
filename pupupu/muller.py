from fractions import Fraction

def f(y, z):
    return 108 - (815 - 1500 / z) / y

x_exact = [Fraction(4), Fraction(17, 4)]
for n in range(2, 51):
    x_exact.append(f(x_exact[n-1], x_exact[n-2]))

print(f"{'i':<3}| {'xi':<30}")
for i in range(51):
    print(f"{i:<3}| {float(x_exact[i]):5f}")
