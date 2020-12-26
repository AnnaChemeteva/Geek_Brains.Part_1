with open('file_5.txt', 'w', encoding='UTF-8') as file:
    numbers = input('Введите любые числа через пробел: ')
    file.write(numbers)
    result = [int(el) for el in numbers.split(' ')]
    print(f'Сумма всех чисел: {sum(result)}')
