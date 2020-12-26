with open('file_6.txt', 'r', encoding='UTF_8') as file:
    result = []
    info_lessons = {}
    for line in file:
        text = str(''.join(c for c in line if c not in ':\n-()')).split(' ')
        result.append(text[0])
        text.remove(text[0])
        text = list(filter(None, text))
        a = []
        for el in text:

            el = el[:-3]
            a.append(int(el))
        result.append(sum(a))
    i = 0
    while i != len(result):
        info_lessons[result[i]] = result[i + 1]
        i += 2

    print(info_lessons)
