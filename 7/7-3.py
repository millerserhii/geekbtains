import math


class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell if self.cell - other.cell > 0 else "Cells are equal or 2'nd is bigger")

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, val):
        result = ""
        for i in range(math.ceil(self.cell/val)):
            if i+1 == math.ceil(self.cell/val) and self.cell % val != 0:
                result += "*" * (self.cell % val)
            else:
                result += "*" * val + "\n"
        return Cell(result)


c1 = Cell(15)
c2 = Cell(13)
#print(c1.make_order(6))
print(c2.make_order(3))
