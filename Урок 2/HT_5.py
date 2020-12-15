i = 0
rating = [3, 6, 1]
while i != 6:
    try:
        user_number = int(input('Введите натуральное число от 1 до 9: '))
    except ValueError:
        print('Введите натуральное число от 1 до 9')
    else:
        if user_number <= 9:
            if user_number in rating:
                print('Это число уже есть')
                i += 1
            else:
                i += 1
                rating.append(user_number)
                rating.sort(reverse=True)
                print(rating)
        else:
            print('Ошибка')

print(rating)
