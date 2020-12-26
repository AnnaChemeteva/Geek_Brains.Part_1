with open('my_file.txt', 'w', encoding='UTF-8') as file:
    while True:
        info = input('Введите текст: \n')
        file.write(info)
        file.write('\n')
        if not info:
            break
