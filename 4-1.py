from sys import argv

name, hours, rate, bonus = argv


def salary(hours, rate, bonus):
    print((hours * rate) + bonus)



salary(int(hours), int(rate), int(bonus))
