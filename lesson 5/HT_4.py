with open('file_4_1.txt', 'r', encoding='UTF - 8') as f:
    with open('file_4_2.txt', 'a', encoding='UTF - 8') as b:
        english = ['One', 'Two', 'Three', 'Four']
        translate = ['Один', 'Два', 'Три', 'Четыре']
        i = 0
        for line in f:
            line = str(line).split(' ')
            if line[0] == english[i]:
                line[0] = translate[i]
                line = ''.join(line)
                b.write(line)
                i += 1
                if i == 4:
                    break
