from itertools import count
from itertools import cycle

counter_count = count(1)
my_list = list(next(counter_count) for _ in range(3))

counter_cycle = cycle(my_list)
new_list = list(next(counter_cycle) for _ in range(10))

print(my_list)
print(new_list)