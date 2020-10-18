day_km = int(input("Enter first day km "))
target_km = int(input("Enter target km "))
day = 1

while target_km > day_km:
    day_km += day_km * 0.1
    day += 1

print(day)



