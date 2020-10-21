
with open ("task1.txt", "w", encoding="utf-8") as f:
    while True:
        usr_text = (input("Enter some text: "))
        if usr_text:
            print(usr_text, file=f)
        else:
            break
