import copy
import csv
from functools import reduce

lst = [
    {"Name": "Ivan", "Age": 35, "Height": 176},
    {"Name": "Bert", "Age": 25, "Height": 178},
    {"Name": "Elly", "Age": 24, "Height": 164},
    {"Name": "Carl", "Age": 42, "Height": 182},
]

with open('./datas/ex8.csv', 'w', encoding='utf-8', newline='') as f:
    l = copy.deepcopy(lst)
    res = csv.DictWriter(f, fieldnames=['Id', 'Name', 'Age', 'Height'], quoting=csv.QUOTE_NONNUMERIC)
    res.writeheader()
    for i, d in enumerate(l, start=1):
        d['Id'] = i
        res.writerow(d)


# способ с генератором полей столбцов
with open('./datas/ex8b.csv', 'w', encoding='utf-8', newline='') as f:
    fn = {key for d in lst for key in d}    # соберет все ключи, даже если они в словарях отличаются
    print(fn)
    res = csv.DictWriter(f, fieldnames=fn, quoting=csv.QUOTE_NONNUMERIC)
    res.writeheader()
    res.writerows(lst)


# способ с лямбдой и reduce
with open('./datas/ex8c.csv', 'w', encoding='utf-8', newline='') as f:
    fn = list(reduce(lambda x, y: x | y.keys(), lst, set()))
    print(fn)
    res = csv.DictWriter(f, fieldnames=fn, quoting=csv.QUOTE_NONNUMERIC)
    res.writeheader()
    res.writerows(lst)
