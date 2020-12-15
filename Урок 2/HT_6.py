products = [
    [1, {'название': ' ', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}],
    [2, {'название': ' ', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}],
    [3, {'название': ' ', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}]
]

info = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
info['название'] = list(info['название'])
info['цена'] = list(info['цена'])
info['количество'] = list(info['количество'])
info['ед'] = list(info['ед'])


def change_info_prod(number, name, price, amount, measure):
    for i in range(number):
        products[i][1][name] = input(f'Введите {name} изделия номер {i + 1}: ')
        info[name].append(products[i][1][name])
        products[i][1][price] = input(f'Введите {price} изделия номер {i + 1}: ')
        info[price].append(products[i][1][price])
        products[i][1][amount] = input(f'Введите {amount} изделия номер {i + 1}: ')
        info[amount].append(products[i][1][amount])
        products[i][1][measure] = input(f'Введите {measure} изделия номер {i + 1}: ')
        info[measure].append(products[i][1][measure])

    info[measure] = list(set(info[measure]))


change_info_prod(3, 'название', 'цена', 'количество', 'ед')


def tup_prod(number):
    for i in range(number):
        products[i] = tuple(products[i])


tup_prod(3)

print(info)
print(products)
