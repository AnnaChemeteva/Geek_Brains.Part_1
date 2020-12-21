import random

test = []

for i in range(10):
    test.append(random.randint(1, 1000))

result = [el for el in test if el > test[test.index(el) - 1] and test.index(el) != 0]

print(test)
print(result)


