import random

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} in move")

    def stop(self):
        print(f"Car {self.name} stoped")

    def turn(self):
        direction = random.choice(["right", "left", "straight ahead", "backwards"])
        print(f"Car {self.name} is going {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
        print(f"{self.speed if self.speed <= 60 else f'Slow down to 60! Your speed is {self.speed}'}")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f"{self.speed if self.speed <= 40 else f'Slow down to 40! Your speed is {self.speed}'}")

class PoliceCar(Car):
    def police(self):
        print(f"You are in police car {self.name}")


car1 = WorkCar(60, "red", "Chevrolet")
car1.go()
car1.turn()
car1.show_speed()
car1.stop()

car2 = PoliceCar(10, "white", "BMW", True)
print(f"Car is police - {car2.is_police}")

car3 = TownCar(100, "black", "Ferrari")
car3.show_speed()