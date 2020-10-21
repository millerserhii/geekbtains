
with open("employees.txt", "r", encoding="utf-8") as f:
    emp_dict = {}
    total_salary = 0
    items = 1
    for line in f:
        line = line.split()
        emp_dict.update({line[0] : line[1]})
    for k, v in emp_dict.items():
        if float(v) < 20000:
            print(f"{k} имеет оклад ${v}")
        total_salary += float(v)
        items += 1
    av_salary = round(total_salary / items, 2)

    print(f"Средняя зарплата по компании - ${av_salary}")








