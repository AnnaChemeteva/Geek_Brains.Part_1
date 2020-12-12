try:
    a = input('Введите любое число: ')
    b = int(a + a)
    c = int(a + a + a)
except ValueError:
    print('Ошибка. Вы ввели не число')
else:
    print(int(int(a) + b + c))
