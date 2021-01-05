class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname}')

    def get_total_income(self, param_1, param_2):
        print(f'Доход сотрудника {param_1 + param_2} ')


worker_1 = Position('Петр', 'Петров', 'менеджер', income={"wage": 10000, "bonus": 1000})
worker_1.Worker__income = {"wage": 10000, "bonus": 1000}
worker_1.get_total_income(worker_1.Worker__income['wage'], worker_1.Worker__income['bonus'])
