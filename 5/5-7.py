import json


with open("task7.txt", "r", encoding="utf-8") as f:
    companies = {}
    total_profit = 0
    companies_count = 0
    for line in f:
        line = line.split()
        companies.update({line[0] : int(line[2])-int(line[3])})
    for x in companies.values():
        if x > 0:
            total_profit += x
            companies_count += 1
    av_profit = {"average_profit" : round(total_profit/companies_count, 1)}
    result = [companies, av_profit]

with open("task7.json", "w", encoding="utf-8") as json_file:
    json.dump(result, json_file, indent=4, ensure_ascii=False)