class Cage:
    def __init__(self, param):
        try:
            self.param = []
            for i in range(param):
                self.param.append(i)
        except TypeError:
            print('Клетка может состоять только из целого количесва ячеек')

    def __add__(self, other):
        return f'Объединение двух клеток: {self.param + other.param}'

    def __sub__(self, other):
        if len(self.param) - len(other.param) > 0:
            return f'Разница двух клеток: {len(self.param) - len(other.param)}'
        else:
            print('Разница ниже нуля')

    def __mul__(self, other):
        return f'Количество ячеек общей клетки равно: {len(self.param) * len(other.param)}'

    def __truediv__(self, other):
        return f'Общая клетка из деления двух содержит {round(len(self.param) / len(other.param))} ячеек'

    def make_oder(self):
        a = []
        b = []
        for el in self.param:

            if len(b) < 3:
                b.append(el)
            else:
                a.append(b)

        return a


cage_1 = Cage(5)
cage_2 = Cage(8)
cage_3 = Cage(2)

print(cage_1.__add__(cage_2))
print(cage_2.__sub__(cage_3))
print(cage_2.__mul__(cage_1))
print(cage_2.__truediv__(cage_3))
print(cage_2.make_oder())
