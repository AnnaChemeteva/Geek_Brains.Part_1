try:
    user_number = int(input('Введите число: '))
except ValueError:
    print('Вы ввели не число')
else:
    print(user_number)

#как здесь настроить обработку исключений? не могу понять какое будет название итсключения

user_words = input('Введите любое слово: ')
print(user_words)

comp_mass = [1,2.3,5,'May']
print(comp_mass)
print(comp_mass[-1])


