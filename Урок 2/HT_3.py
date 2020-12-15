try:
    month = int(input('Введите число: '))
except ValueError:
    print('Введите число')
else:
    year = {
        1: 'winter',
        2: 'winter',
        3: 'spring',
        4: 'spring',
        5: 'spring',
        6: 'summer',
        7: 'summer',
        8: 'summer',
        9: 'autumn',
        10: 'autumn',
        11: 'autumn',
        12: 'winter'
    }

    if month in year.keys():
        print(year[month])

    spring = [3, 4, 5]
    winter = [12, 1, 2]
    autumn = [9, 10, 11]
    if month in spring:
        print('spring')
    elif month in winter:
        print('winter')
    elif month in autumn:
        print('autumn')
    else:
        print('summer')
