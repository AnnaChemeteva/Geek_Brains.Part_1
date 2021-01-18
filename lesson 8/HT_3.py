#не доделала

class TextException(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    array_user = []

    try:
        elem = input('Введите элемент для формирования списка чисел: ')

        if int(elem) == int(elem):
            array_user.append(elem)
        elif elem == 0:
            print(array_user)
            break
        else:
            raise ValueError('Вы ввели не число')
    except ValueError as e:
        print(e)


