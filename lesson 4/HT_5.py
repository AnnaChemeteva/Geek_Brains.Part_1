from functools import reduce


def product(el_1, el_2):
    return el_1 * el_2


test = [n for n in range(99, 1001) if n % 2 == 0]

result = reduce(product, test)
print(result)
