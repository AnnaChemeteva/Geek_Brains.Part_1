import math


def func(n):
    for el in range(1, n):
        yield el
    a = math.factorial(n)
    print(a)


print(func(4))

for i in func(4):
    print(i)
