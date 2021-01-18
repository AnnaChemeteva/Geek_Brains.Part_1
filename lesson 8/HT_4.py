class Store:
    def __init__(self, main):
        self.main = main


class Equipment:
    def __init__(self, quantity, mark):
        self.quantity = quantity
        self.mark = mark

    def acceptance(self):
        self.mark = input('Введите название техники: ')
        try:
            self.quantity = int(input('Введите количество единиц: '))
        except ValueError:
            return 'Введите число'
        else:

            if self.mark == 'Сканер':
                office_1['Оборудование'] = self.mark
                office_1['Количество'] = self.quantity
                return f'В первый офис было отправлено: {office_1}'
            else:
                office_2['Оборудование'] = self.mark
                office_2['Количество'] = self.quantity
                return f'Во второй офис было отправлено: {office_2}'



class Printer(Equipment):
    def __init__(self, print_color, size_of_paper):
        self.print_color = print_color
        self.size_of_paper = size_of_paper

    def color_print(self):
        office_2['Тип принтера по печати'] = self.print_color
        return f'Во второй офис было отправлено:  {office_2}'


class Scanner(Equipment):
    def __init__(self, has_copy):
        self.has_copy = has_copy

    def copy_scanner(self):
        office_1['Возможность делать копии'] = self.has_copy
        return f'В первый офис было отправлено: {office_1}'


class Xerox(Equipment):
    def __init__(self, has_scanner):
        self.has_scanner = has_scanner

    def scanner_copy(self):
        office_2['Возможность сканировать'] = self.has_scanner
        return f'Во второй офис было отправлено: {office_2}'





office_1 = {}
office_2 = {}

scanner_1 = Scanner('Да')
printer_1 = Printer

print(scanner_1.acceptance())
print(scanner_1.copy_scanner())
