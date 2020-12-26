with open('file_2.txt', 'r', encoding="UTF-8") as file:
    i = 0
    for line in file:
        i += 1
        line = str(line).split(' ')
        print(f'В {i} строке содержится {len(line)} элемента')
    print(f'Всего строк в файле: {i}')
