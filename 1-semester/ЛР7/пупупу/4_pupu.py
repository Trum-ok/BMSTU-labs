import re

alp = frozenset({'Z', 'P', 'V', 'X', 'M', 'J', 'W', 'H', 'D', 'T', 'R', 'F', 'C', 'S', 'G', 'B', 'L', 'Q', 'N', 'K'})
lst = input("Введите элементы списка через пробел: ").split()

lst = [re.sub(r'|'.join(alp), lambda x: x.group(0).lower(), word) for word in lst]

print(lst)
