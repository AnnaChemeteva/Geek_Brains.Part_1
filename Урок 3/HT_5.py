def summ_number(new):
    l = []
    length = len(new)
    for i in range(length):
        new[i] = int(new[i])
        l.append(new[i])
        i += 1
    return sum(l)


new_list = input('Введите любое количество чисел через пробел: ').split()
all = []
all.append(summ_number(new_list))
print(sum(all))

while True:

    user_answer = input('Вы хотите продолжить? Есди да, то +. Если нет, то - : ')
    if user_answer == '+':
        new_list = input('Введите любое количество чисел через пробел: ').split()
        all.append(summ_number(new_list))
        print(sum(all))
    else:
        print(f'Общая сумма всех введенных чисел: {sum(all)}')
        break
