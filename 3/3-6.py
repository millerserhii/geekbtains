
def int_func1(user_input):
    print(user_input)
    usr_list = user_input.split()
    copy_list = usr_list.copy()
    """Цикл для отсеивания из списка недопустимых символов"""
    for i in usr_list:
        for a in i:
            if ord(a) not in range(97, 123):
                copy_list.remove(i)
                break
    final_str = " ".join(copy_list).title()
    return final_str


print(int_func1(input("Enter few words: ")))
