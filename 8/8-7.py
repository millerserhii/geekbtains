class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'Complex = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Complex = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'Complex = {self.a} + {self.b} * i'


c1 = Complex(1, -2)
c2 = Complex(3, 4)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)