"""
Задание №6.

Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import csv
import os.path
import pickle


def pickle_2_csv(src, dst):
    if os.path.exists(src):
        with open(src, 'rb') as f:
            res = pickle.load(f)
        # составляем список ключей
        keys = {key for d in res for key in d.keys()}
        # пишем в csv-файл
        with open(dst, 'w', newline='', encoding='utf-8') as f:
            out = csv.DictWriter(f, fieldnames=keys, restval="-", dialect='excel', quoting=csv.QUOTE_MINIMAL)
            out.writeheader()
            out.writerows(res)

    else:
        print(f"Error: file {src} not found!")


if __name__ == '__main__':
    pickle_2_csv('./datas/ex4.pickle', './datas/ex6.csv')
