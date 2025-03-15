"""
Задание №4.

Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""
import csv
import json
import os.path


def correct_csv(src, dst):
    if os.path.exists(src):
        with open(src, 'r', newline='', encoding='utf-8') as f:
            d = csv.reader(f)
            lst = [el for el in d]
        # конвертируем
        res = list()
        keys = lst[0]  # названия ключей
        for i in range(1, len(lst)):
            l = lst[i]
            l[1] = l[1].rjust(10, '0')
            l[2] = l[2].title()
            res.append({keys[0]: l[0], keys[1]: l[1], keys[2]: l[2], "hash": hash(f"{l[1]}{l[2]}")})
        # пишем результат
        with open(dst, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=2, sort_keys=True)
    else:
        print(f"Error: file '{src}' not found!")


if __name__ == '__main__':
    correct_csv('./datas/ex2.csv', './datas/ex4.json')
