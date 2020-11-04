class MyException(Exception):
    def __init__(self, text):
        self.text = text


my_lst = []
while len(my_lst) < 5:
    try:
        digit = input("Enter num: ")
        if not digit.isdigit():
            raise MyException("This is not digit")
        my_lst.append(digit)
    except MyException as err:
        print(err)
    print(my_lst)
