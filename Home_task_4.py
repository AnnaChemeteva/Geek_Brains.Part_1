# вариант без цикла
try:
    b = int(input('Введите число: '))
except ValueError:
    print('Ошибка. Вы ввели не число')
else:
    print(max(str(b)))

# вариант с циклом(смогла решить только с помощью интернета)
try:
    a = int(input('Введите число: '))
except ValueError:
    print('Ошибка. Вы ввели не число')
else:
    max_number = a % 10
    a = a // 10
    while a > 0:
        if a % 10 > max_number:
            max_number = a % 10
        a = a // 10
    print(max_number)
