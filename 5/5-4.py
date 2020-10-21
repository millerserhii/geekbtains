from googletrans import Translator


with open("translate_en.txt", "r", encoding="utf-8") as en_file:
    for line in en_file:
        en_word = (line.split()[0])
        translator = Translator()
        ru_word = translator.translate(en_word, dest="ru").text
        print(ru_word)
        with open("translate_ru.txt", "a", encoding="utf-8") as ru_file:
            ru_file.write(f"{ru_word} {line.split()[1]} {line.split()[2]}\n")





