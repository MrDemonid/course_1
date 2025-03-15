"""
Задание №3.

Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""

import csv
import json
import os.path
from json import JSONDecodeError


def conv_json_2_csv(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            try:
                d: dict = json.load(f)
            except JSONDecodeError:
                d = dict()
        if len(d) > 0:
            # сохраняем в csv
            name = os.path.splitext(file_name)[0] + '.csv'
            with open(name, 'w', newline='', encoding='utf-8') as f:
                res = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
                res.writerow(['level', 'id', 'name'])
                for k in d.keys():
                    line: dict = d[k]
                    for key, v in line.items():
                        res.writerow([k, key, v])
                        print(f"  -- add {[k, key, v]}")
        else:
            print("Error: dictionary is empty!")
    else:
        print("Error: file not found!")


if __name__ == '__main__':
    conv_json_2_csv('./datas/ex2.json')
