with open('file_3.txt', 'r', encoding='UTF-8') as file:
    a = []
    b = []
    for line in file:
        line = str(line).split(' ')
        b.append(int(line[1]))
        if line[1] <= '20000':
            a.append(line[0])
    print(f'Оклад ниже 20 тыс у {a}')
    print(f'Средняя зп у сотрудников: {sum(b)/ len(line)}')
