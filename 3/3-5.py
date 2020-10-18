
def string_func():
    summ = 0
    while True:
        user_input = input("Введите числа через пробел или 'q' для выхода: ")
        int_input = []
        try:
            if user_input.lower().count("q") == 0:
                user_input = user_input.split()
                for i in user_input:
                    int_input.append(int(i))
                summ += sum(int_input)
                print(summ)
                continue
            elif user_input.lower().endswith('q') and len(user_input.lower()) > 1:
                user_input = user_input.replace("q", "")
                user_input = user_input.split()
                for i in user_input:
                    int_input.append(int(i))
                summ += sum(int_input)
                print(summ)
                print("Program finished")
                break
            else:
                print("Program finished")
                break
        except ValueError:
            print("Enter valid number or q for quit")
    return summ


string_func()
