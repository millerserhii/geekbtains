
class Road:

    def __init__(self, _width, _lenght):
        self.lenght = _lenght
        self.width = _width

    def weight(self):
        total_weight = self.width * self.lenght * 0.025 * 5
        print(f"Общий вес дороги - {total_weight} т")

first_road = Road(10, 5000)
first_road.weight()


