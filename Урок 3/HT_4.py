def exponentiation(x, y):
    i = 0
    a = x * x
    for i in range(-(y + 2)):
        i += 1
        a *= x
    return 1 / a


def easy_exponentiation(x, y):
    return x ** y


c = int(input('Введите любое положительное число: '))
b = int(input('Введите любое отрицательное число: '))

print(exponentiation(c, b))
print(easy_exponentiation(c, b))
