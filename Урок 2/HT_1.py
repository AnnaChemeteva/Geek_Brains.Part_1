a = [11, 3, 6, 1.2, 'asd', {1: 'cat'}]
print(a)

a.append('Hello')
a.append(123)
a.append(1.8)

print(a)

for i, el in enumerate(a):
    print(f'{i}: {type(el)}')
