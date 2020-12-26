import json

with open('file_7.txt', 'r', encoding='UTF-8') as file:
    company = []
    average_profit = []
    final_info = {}
    average_profit_final = {}
    for line in file:
        info = str(''.join(c for c in line if c not in ':\n-()')).split(' ')
        company.append(info[0])
        info = info[2:]
        a = int(info[0]) - int(info[1])
        if a > 0:
            company.append(a)
            average_profit.append(a)
        else:
            company.append(a)
    i = 0
    while i != len(company):
        final_info[company[i]] = company[i + 1]
        i += 2

    average_profit_final['average_profit'] = sum(average_profit)

    result = [final_info, average_profit_final]
    print(result)

with open('file.json.txt', 'w', encoding='UTF-8') as file:
    json.dump(result, file, ensure_ascii=False)
