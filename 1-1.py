name = "Serhii"
age = 28


print(f"My name is {name}, i'm {age}.")

new_name = input("What's your name? ")
new_age = int(input("What's your age? "))

if new_age > age:
    print(f"Hey, {new_name}, you are {new_age} and you are older then me")
elif new_age < age:
    print(f"Hey, {new_name}, you are {new_age} and I'm older then you")
else:
    print(f"Hey, {new_name}, you are {new_age} and we are peers")

