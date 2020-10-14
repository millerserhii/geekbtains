
def my_func(*args):
    s = sorted(args)
    return s[-1]+s[-2]


print(my_func(7, 9, 5))
