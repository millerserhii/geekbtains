
user_input = input("Enter few words ")

string = user_input.split()

for i in range(len(string)):
    new_str = string[i]
    print(f"{i+1} - {new_str[:10]}")
