import csv

# Десериализация из CSV-файла

with open("./datas/ex6.csv", 'r', encoding='utf-8', newline='\n') as f:
    fn = csv.reader(f)
    # print(*fn)
    for s in fn:
        print(s)
print('-------------------------')


# Чтение в словарь.
with open("./datas/ex6.csv", 'r', encoding='utf-8', newline='\n') as f:
    res = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
    for s in res:
        print(s)

print('-------------------------')
with open("./datas/ex6.csv", 'r', encoding='utf-8', newline='\n') as f:
    res = csv.DictReader(f, fieldnames=['Имя', 'Пол', 'Возраст', 'Высота', 'office'], restkey='new', restval='def value')
    for s in res:
        print(s)

print('-------------------------')
with open("./datas/ex6.csv", 'r', encoding='utf-8', newline='\n') as f:
    res = csv.DictReader(f, fieldnames=['Имя', 'Пол'], restkey='new', restval='def value')
    for s in res:
        print(s)
