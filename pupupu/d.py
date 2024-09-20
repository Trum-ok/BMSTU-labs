# Element = ['Na', 'C', 'O']
# A=[23,12,16]
# K=[2,1,3]

# M=0
# for i in range(len(Element)):
#     M += A[i]*K[i]
#     print(f"{Element[i]} * {A[i]} * {K[i]} = {A[i]*K[i]}")
# print(f"Mr(Na2CO3) = {M}")

Element=[ ['Na', 23,2], ['C', 12,1], ['0', 16,3]]

M=0
for i in Element:
    print(i)
    M += i[1]*i[2]
print(M)
