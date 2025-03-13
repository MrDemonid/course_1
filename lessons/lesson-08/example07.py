import csv

# lst = [
#     {"Name": "Ivan", "Age": 35, "Height": 176},
#     {"Name": "Bert", "Age": 25, "Height": 178},
#     {"Name": "Elly", "Age": 24, "Height": 164},
#     {"Name": "Carl", "Age": 42, "Height": 182},
# ]

# Запись CSV

lst = [
    ["Name", "Age", "Height"],
    ["Ivan N", 35, 176],
    ["Bert", 25, 178],
    ["Elly", 24, 164],
    ["Carl", 42, 182],
]

with open('./datas/ex7.csv', 'w', newline='') as f:
    wr = csv.writer(f, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for d in lst:
        print(d)
        wr.writerow(d)

with open('./datas/ex7b.csv', 'w', newline='') as f:
    wr = csv.writer(f, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    wr.writerows(lst)


