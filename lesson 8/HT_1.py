class Data:
    def __init__(self, day):
        self.day = day

    @classmethod
    def data_int(cls, self):
        a = self.day.split('.')
        day = []
        for i in a:
            day.append(int(i))

        return day

    @staticmethod
    def data_val(self):
        a = self.day.split('.')
        day = []
        for i in a:
            day.append(int(i))
        if 1 > day[0] > 31:
            return 'Ошибка. День неверный'
        elif day[1] > 12:
            return 'Ошибка. Месяц неверный'
        elif day[2] > 2021:
            return 'Ошибка. Год неверный'
        else:
            return day


data_1 = Data('25.08.2020')
data_2 = Data('01.17.2030')
print(data_1.data_int(data_1))
print(data_2.data_val(data_2))
