
def divfunc():
    try:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        return (f"{x / y}")
    except ZeroDivisionError:
        return ("Division on 0 is impossible")
    except ValueError:
        return ("Enter valid number")


print(divfunc())
