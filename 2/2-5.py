
my_list = [7, 5, 3, 3, 2]
new_rating = int(input("Enter new rating: "))
reversed_list = my_list[::-1]

if new_rating in reversed_list:
    rating_index = reversed_list.index(new_rating)
    reversed_list.insert(rating_index, float(new_rating))
elif new_rating < min(reversed_list):
    reversed_list.insert(0, float(new_rating))
else:
    reversed_list.append(float(new_rating))

my_list = reversed_list[::-1]
print(my_list)
