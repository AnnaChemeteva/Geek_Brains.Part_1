import time


class TrafficLight:
    def __init__(self, color):
        self.color = color

    def switch_on(self, param_1, param_2, param_3):
        if param_1 == 'красный' and param_2 == 'желтый' and param_3 == 'зеленый':
            print(f'Свет переключен на красный.')
            time.sleep(7)
            print(f'Свет переключен на желтый.')
            time.sleep(2)
            print(f'Свет переключен на зеленый.')
            time.sleep(3)
            print(f'Светофор закончил работу.')
        else:
            print('Неверная последвательность включения света.')


light = TrafficLight('красный')
light.switch_on('красный', 'желтый', 'зеленый')
