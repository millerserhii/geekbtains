
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отприсовки")

class Pen(Stationery):
    def draw(self):
        print(f"Ручка рисует {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Карандаш рисует {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Маркер рисует {self.title}")


pen = Pen("круг")
pen.draw()

pencil = Pencil("квадрат")
pencil.draw()

marker = Handle("треугольник")
marker.draw()