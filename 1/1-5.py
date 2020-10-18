
income = int(input("Enter income of the company "))
costs = int(input("Enter costs of the company "))
pnl = income-costs

if pnl > 0:
    profit = float(f"{income/pnl:.2f}")
    employees = int(input("Enter number of employees "))
    ppe = float(f"{pnl/employees:.2f}")
    print(f"Profitability is {profit}, Net profit per 1 employee is {ppe}")
else:
    print(f"Your companies PNL is {pnl}")