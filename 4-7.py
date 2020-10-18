import math


def generator(x):
    for el in range(1, x+1):
        yield el

factorial = 1
usr_input = int(input("Введите число "))

for i in generator(usr_input):
    factorial *= i

print(factorial)
print(math.factorial(usr_input))