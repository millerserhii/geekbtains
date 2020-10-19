
first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]

new_list = [el for num, el in enumerate(first_list) if el > first_list[num-1] and first_list[num] != first_list[0]]

print(first_list)
print(new_list)
