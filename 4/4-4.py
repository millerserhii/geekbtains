
first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [x for x in first_list if first_list.count(x) == 1]

print(result)