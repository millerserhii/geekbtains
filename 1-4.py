
number = int(input("Enter number "))
max_num = 0

while number:
    last_digit = number % 10
    number = (number - last_digit)//10
    if last_digit > max_num:
        max_num = last_digit

print(max_num)

