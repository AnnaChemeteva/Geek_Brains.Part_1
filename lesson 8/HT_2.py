class ExceptException(Exception):
    def __init__(self, txt):
        self.txt = txt


numb_1 = int(input('Введите кратное число: '))
numb_2 = int(input('Введите делитель кратного числа: '))

try:
    if numb_2 == 0:
        raise ExceptException('На ноль делить нельзя')
    else:
        print(numb_1//numb_2)
except ExceptException as e:
    print(e)
