try:
    a = input('Введите предложение: ').split()
except ValueError:
    "Введите слова"
else:
    count = 0
    for i in a:
        count += 1
        print(f'{count}: {i[:11]}')
