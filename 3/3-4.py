
def my_func(x, y):
    return x**y


def my_func1(x, y):
    result = 0
    if y < 0:
        y = y * -1
        for _ in range(y-1):
            if result == 0:
                result = x * x
            else:
                result = result * x
        result = 1/result
    else:
        for _ in range(y-1):
            if result == 0:
                result = x * x
            else:
                result = result * x
    return result


print(my_func(12, -2))
print(my_func1(12, -2))
