def division(x, y):
    try:
        a = x / y
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
    else:
        return a


print(division(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
