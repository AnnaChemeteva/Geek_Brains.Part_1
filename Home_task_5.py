try:
    proceeds = int(input('Введите выручку вашей компании за год: '))
    costs = int(input('Введите издержки вашей компании за год: '))
except ValueError:
    print('Ошибка. Вы ввели не число')
else:
    if proceeds > costs:
        profit = int(proceeds - costs)
        print(f'Вы работаете не в ноль. Прибыль вашей компании составляет: {profit}')
        persons = int(input('Давайте расчитаем доход на каждого сотрудника. Введите численность штата компании: '))
        profit_per_person = int(profit // persons)
        print(f'Каждый сотрудник приносит вам по {profit_per_person} рублей чистой прибыли.')
    elif proceeds == costs:
        print('Печально. Вы работаете в ноль. Пересмотрите бизнес-план.')
    else:
        print('Вы точно бизнесмен? Ваша компания убыточна')
