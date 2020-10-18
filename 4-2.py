
first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]

new_list = [x for x in first_list if x > first_list[first_list.index(x) - 1]]

print(first_list)
print(new_list)
