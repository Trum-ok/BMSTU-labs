x = float(input("x: "))
eps = float(input("eps: "))

n = 1
term = 1/6
sums = term

mxn = (x)**n

while (abs(term) >= eps):
    print(term)
    term *= mxn
    term /= ((2*n + 2) * (2*n + 3))
    print(sums)
    sums += term
    n += 1

print(sums)
