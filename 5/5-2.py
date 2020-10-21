
with open("task1.txt", "r", encoding="utf-8") as f:
    lines = 0
    for line in f:
        lines +=1
        print(f"Строка {lines} имеет {line.count('')-2} символов")  # -2 это вычитаем перенос каретки \n
    print(f"В файле {lines} строк")
