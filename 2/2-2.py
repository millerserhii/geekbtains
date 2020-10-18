
dict = {k: input("Enter value ") for k in range(6)}
new_dict = dict.copy()

for i in range(0, len(dict), 2):
    if len(dict) % 2 == 0:
        dict[i] = dict[i + 1]
        dict[i + 1] = new_dict[i]
    else:
        if i < len(dict)-1:
            dict[i] = dict[i + 1]
            dict[i + 1] = new_dict[i]
        else:
            dict[i] == len(dict)

print(dict)







