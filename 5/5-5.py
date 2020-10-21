with open("task5.txt", "w+", encoding="utf-8") as file:
    for i in range(1, 21):
        file.write(f"{i} ")
    file.seek(0)
    text = file.read().split()
    summary = 0
    for i in text:
        summary += int(i)
    print(summary)

