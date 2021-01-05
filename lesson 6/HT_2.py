class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asfalt(self, a, b):
        mass = self._length * self._width * a * b
        print(f'Для покрытия данной дороги вам необходимо {mass} кг асфальта')


road_1 = Road(1000, 200)
road_1.asfalt(25, 5)
