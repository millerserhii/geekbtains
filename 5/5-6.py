import re


with open("task6.txt", "r", encoding="utf-8") as file:
    lessons_dict = {}
    final_dict = {}
    for line in file:
        line = line.replace("\n", "").split(":")
        lessons_dict.update({line[0]: line[1]})
    for k, v in lessons_dict.items():
        hours = sum([int(i) for i in re.findall(r'\d+', v)])
        final_dict.update({k:hours})

print(final_dict)
