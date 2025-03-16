"""
Задача 2. Объединение данных из нескольких JSON файлов.

Напишите скрипт, который объединяет данные из нескольких JSON файлов в один.
Каждый файл содержит список словарей, описывающих сотрудников компании (имя, фамилия, возраст, должность).
Итоговый JSON файл должен содержать объединённые списки сотрудников из всех файлов.

Пример:
У вас есть три файла employees1.json, employees2.json, employees3.json.
Нужно объединить их в один файл all_employees.json.
"""
import json
from pathlib import Path


def join_jsons(src_dir, dst_file):
    src = Path(src_dir).resolve()
    res = list()
    for fn in src.rglob('*.json'):
        print(f"  -- found: {fn}")
        with open(fn, 'r', encoding='utf-8') as f:
            lst = list(json.load(f))
        res += lst
    if len(res) > 0:
        with open(dst_file, 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=True, ensure_ascii=False)


if __name__ == '__main__':
    join_jsons('./datas/zad_2', './datas/all_employees.json')

