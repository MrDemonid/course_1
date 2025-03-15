"""
Задание №7.

Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import os.path
import pickle

from memory_profiler import profile

@profile
def csv_2_pickle(src):
    if os.path.exists(src) and os.path.isfile(src):
        with open(src, 'r', newline='', encoding='utf-8') as f:
            # lst = list(csv.reader(f))
            lst = [*csv.reader(f)]
            print(lst)
        res = pickle.dumps(lst)
        print(res)

    else:
        print(f"Error: file {src} not found!")


if __name__ == '__main__':
    csv_2_pickle('./datas/ex6.csv')
