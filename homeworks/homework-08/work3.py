"""
Задача 3. Агрегирование данных из CSV файла.

Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV файл.
JSON файл содержит данные о продуктах (название, цена, количество на складе).
В CSV файле каждая строка должна соответствовать одному продукту.

Пример: Из файла products.json нужно создать products.csv.
"""
import csv
import json
from pathlib import Path


def json_2_csv(src_file):
    src = Path(src_file).resolve()
    if src.exists() and src.is_file():
        with open(src, 'r', encoding='utf-8') as f:
            lst = list(json.load(f))

    # Проверка корректности формата данных
    if not isinstance(lst, list) or not all(isinstance(item, dict) for item in lst):
        raise ValueError(f"Error: bad json-data format!")

    name = src.with_suffix('.csv')
    with open(name, 'w', newline='', encoding='utf-8') as f:
        keys = {key for d in lst for key in d.keys()}
        wr = csv.DictWriter(f, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
        wr.writeheader()
        wr.writerows(lst)


if __name__ == '__main__':
    json_2_csv('./datas/zad_3/products.json')
