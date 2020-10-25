
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"{sum(self.income.values())}")

worker_1 = Position("John", "Golt", "CEO", {"wage":100000, "bonus":40000})
worker_1.get_full_name()
worker_1.get_total_income()
print(worker_1.position)

