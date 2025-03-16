"""
Задание 1. Работа с основными данными.

Напишите функцию, которая получает на вход директорию и рекурсивно обходит
её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
pickle. Для дочерних объектов указывайте родительскую директорию. Для
каждого объекта укажите файл это или директория. Для файлов сохраните его
размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
задания функций пакет для работы с файлами разных форматов.
"""
import csv
import json
import os
import pickle


def _do_scan_path(root, lst: list):
    """
    Обход всех путей.
    Данные о файлах и подкаталогах складывает в lst.
    Вернет общий размер root, включая подкаталоги.
    """
    size = 0
    all_elem = os.listdir(root)
    for el in all_elem:
        name = os.path.join(root, el)
        print(f"  -- scan {name}")
        if os.path.isdir(name):
            el_size = _do_scan_path(name, lst)
            size += el_size
            lst.append(
                {
                    "name": el,
                    "path": name,
                    "type": 'directory',
                    'size': el_size,
                    'parent': os.path.basename(root)
                })
        elif os.path.isfile(name):
            size += os.path.getsize(name)
            lst.append(
                {
                    "name": el,
                    "path": name,
                    "type": 'file',
                    'size': os.path.getsize(name),
                    'parent': os.path.basename(root)
                }
            )
    return size

def scan_directory(directory) -> list[dict]:
    lst = list()
    total = _do_scan_path(directory, lst)
    lst.append(
        {
            "name": directory,
            "path": '',
            "type": 'directory',
            'size': total,
            'parent': ''
        })
    return lst


def save_json(file_name, lst: list[dict]):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(lst, f, ensure_ascii=False, sort_keys=True, indent=2)

def save_csv(file_name, lst: list[dict]):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        keys = {k for d in lst for k in d.keys()}
        wr = csv.DictWriter(f, fieldnames=keys, restval='-', quoting=csv.QUOTE_NONNUMERIC)
        wr.writeheader()
        wr.writerows(lst)

def save_picle(file_name, lst: list[dict]):
    with open(file_name, 'wb') as f:
        pickle.dump(lst, f)


if __name__ == '__main__':
    res = scan_directory('..\\homework-07')
    save_json('.\\datas\\scan.json', res)
    save_csv('.\\datas\\scan.csv', res)
    save_picle('.\\datas\\scan.picle', res)

