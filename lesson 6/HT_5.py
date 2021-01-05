class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'У меня есть {self.title}, делаю им заполнение картины')


class Pen(Stationery):
    def draw(self):
        print(f'У меня есть {self.title}, линия выходит тонкой. Использую для отрисовки контура')


class Handle(Stationery):
    def draw(self):
        print(f'У меня есть {self.title}, идет отрисовка тени')


art_1 = Pen('Ручка')
art_1.draw()

art_2 = Handle('Серый маркер')
art_2.draw()

art_3 = Pencil('Мягкий карандаш')
art_3.draw()
