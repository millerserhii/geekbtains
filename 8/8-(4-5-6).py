class Warehouse:
    def __init__(self, model, qty, price, name):
        self.model = model
        self.qty = qty
        self.price = price
        self.name = name

    printer_list = []
    scanner_list = []
    xerox_list = []

    def add(self):
        new_dict = {"Model": self.model, "Qty": self.qty, "Price": self.price}
        if self.name == "Printer":
            self.printer_list.append(new_dict)
        elif self.name == "Scanner":
            self.scanner_list.append(new_dict)
        else:
            self.xerox_list.append(new_dict)

    @staticmethod
    def printer_audit():
        printer_names = []
        printer_amount = 0
        printer_value = 0
        for i in Warehouse.printer_list:
            printer_names.append(i.get('Model'))
            printer_amount += i.get("Qty")
            printer_value += i.get("Price")
        return f"Printer models - {printer_names}\n" \
               f"Total printers amount - {printer_amount}\n" \
               f"Total printers value - ${printer_value * printer_amount}\n"

    @staticmethod
    def scanner_audit():
        scanner_names = []
        scanner_amount = 0
        scanner_value = 0
        for i in Warehouse.scanner_list:
            scanner_names.append(i.get('Model'))
            scanner_amount += i.get("Qty")
            scanner_value += i.get("Price")
        return f"Scanner models - {scanner_names}\n" \
               f"Total scanner amount - {scanner_amount}\n" \
               f"Total scanner value - ${scanner_value * scanner_amount}\n"

    @staticmethod
    def xerox_audit():
        xerox_names = []
        xerox_amount = 0
        xerox_value = 0
        for i in Warehouse.xerox_list:
            xerox_names.append(i.get('Model'))
            xerox_amount += i.get("Qty")
            xerox_value += i.get("Price")
        return f"Xerox models - {xerox_names}\n" \
               f"Total xerox amount - {xerox_amount}\n" \
               f"Total xerox value - ${xerox_value * xerox_amount}\n"

    @staticmethod
    def total_audit():
        return f"{Warehouse.printer_audit()}\n" \
               f" {Warehouse.scanner_audit()}\n" \
               f" {Warehouse.xerox_audit()}\n"

    @staticmethod
    def remove(tech_list):
        if tech_list == 1:
            for el, item in enumerate(Warehouse.printer_list):
                print(f"{el+1} - {item}")
            usr_input = int(input("Enter item to delete: "))
            Warehouse.printer_list.pop(usr_input-1)
            print("Printer removed")
        elif tech_list == 2:
            for el, item in enumerate(Warehouse.scanner_list):
                print(f"{el+1} - {item}")
            usr_input = int(input("Enter item to delete: "))
            Warehouse.scanner_list.pop(usr_input-1)
            print("Scanner removed")
        elif tech_list == 3:
            for el, item in enumerate(Warehouse.xerox_list):
                print(f"{el+1} - {item}")
            usr_input = int(input("Enter item to delete: "))
            Warehouse.xerox_list.pop(usr_input-1)
            print("Xerox removed")


class Technic:
    def __init__(self, model, qty, price):
        self.model = model
        self.qty = qty
        self.price = price


class Printer(Technic):
    def __init__(self, model, qty, price, name="Printer"):
        super().__init__(model, qty, price)
        self.name = name


class Scanner(Technic):
    def __init__(self, model, qty, price, name="Scanner"):
        super().__init__(model, qty, price)
        self.name = name


class Xerox(Technic):
    def __init__(self, model, qty, price, name="Xerox"):
        super().__init__(model, qty, price)
        self.name = name


while True:
    usr_menu = input("Main warehouse menu:\n"
                     "Enter '1' - adding technic\n"
                     "Enter '2' - deleting technic\n"
                     "Enter '3' - Total audit\n"
                     "Enter '4' - Printers audit\n"
                     "Enter '5' - Scanners audit\n"
                     "Enter '6' - Xerox audit\n"
                     "Enter 'Q' - quit \n")
    if usr_menu == "1":
        try:
            tech_amount = int(input("Enter total tech amount you want to add: "))
        except ValueError:
            "Only numbers"

        for _ in range(tech_amount):
            tech_type = int(input("To add printer - enter '1' \n"
                                  "To add scanner - enter '2' \n"
                                  "To add xerox - enter '3' "))
            tech_model = input("Enter model: ")
            tech_quantity = int(input("Enter quantity: "))
            tech_price = int(input("Enter price: "))
            if tech_type == 1:
                printer = Printer(tech_model, tech_quantity, tech_price)
                Warehouse(printer.model, printer.qty, printer.price, printer.name).add()
                print("item was successfully added")
            elif tech_type == 2:
                scanner = Scanner(tech_model, tech_quantity, tech_price)
                Warehouse(scanner.model, scanner.qty, scanner.price, scanner.name).add()
                print("item was successfully added")
            elif tech_type == 3:
                xerox = Xerox(tech_model, tech_quantity, tech_price)
                Warehouse(xerox.model, xerox.qty, xerox.price, xerox.name).add()
                print("item was successfully added")
            else:
                print("You've entered wrong number, try again")

    elif usr_menu == "2":
        tech_type = int(input("To delete printer - enter '1' \n"
                              "To delete scanner - enter '2' \n"
                              "To delete xerox - enter '3' "))
        Warehouse.remove(tech_type)

    elif usr_menu == "3":
        print(Warehouse.total_audit())
    elif usr_menu == "4":
        print(Warehouse.printer_audit())
    elif usr_menu == "5":
        print(Warehouse.scanner_audit())
    elif usr_menu == "6":
        print(Warehouse.xerox_audit())
    elif usr_menu.upper() == "Q":
        print("Program stopped")
        break
    else:
        print("Enter valid symbol")
