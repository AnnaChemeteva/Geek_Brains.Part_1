class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_right(self):
        print('Машина повернула направо')

    def turn_left(self):
        print('Машина повернула налево')

    def show_speed(self):
        print(f'Скорость машины {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость!')
        else:
            print(f'Скорость машины {self.speed}')


class SportCar(Car):
    def sport(self):
        print('Вы в спортивной машине')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость!')
        else:
            print(f'Скорость машины {self.speed}')


class PoliceCar(Car):

    def police(self):
        if self.is_police == True:
            print('Вы в полицейской машине')
        else:
            print('Вы не в полицейской машине')


auto_1 = TownCar(80, 'черная', 'kia', False)
auto_1.show_speed()
print(auto_1.name)

auto_2 = WorkCar(35, 'красно-белая', 'ВАЗ', False)
auto_2.show_speed()

auto_3 = PoliceCar(55, 'красно-синяя', 'лада', True)
auto_3.police()

