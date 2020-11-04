class MyException(Exception):
    def __init__(self, text):
        self.text = text


first_num = int(input("Enter first num"))
second_num = int(input("Enter second num"))

try:
    if second_num == 0:
        raise MyException("Division by Zero is forbidden")
    result = first_num / second_num
except MyException as err:
    print(err)
else:
    print(result)
