from functools import reduce


my_list = [x for x in range(100, 1001) if x%2 == 0]

print(reduce(lambda prev_el, el: prev_el * el, my_list))