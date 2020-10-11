
user_input = int(input("Enter number of the month: "))

months_list = [{1: "January"}, {2: "February"}, {3: "March"}, {4: "April"}, {5: "May"},
               {6: "June"}, {7: "July"}, {8: "August"}, {9: "September"}, {10: "October"},
               {11: "November"}, {12: "December"}]

winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
autumn = ["September", "October", "November"]

for i in months_list:
    if i.get(user_input) != None:
        month = i.get(user_input)

if month in winter:
    print(f"{user_input} month is {month}, it is winter")
elif month in spring:
    print(f"{user_input} month is {month}, it is spring")
elif month in summer:
    print(f"{user_input} month is {month}, it is summer")
elif month in autumn:
    print(f"{user_input} month is {month}, it is autumn")


