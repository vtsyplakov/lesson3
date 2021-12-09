import csv

dict_personally = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('dict_personally.csv', 'w', encoding='utf-8', newline='') as dict_csv:
    fields = ['name', 'age', 'job']
    writer_csv = csv.DictWriter(dict_csv, fields, delimiter=';')
    writer_csv.writeheader()
    for user in dict_personally:
        writer_csv.writerow(user)