"""
Задача 4. Агрегирование данных из CSV файла.

Напишите скрипт, который считывает данные из CSV файла, содержащего информацию о
продажах (название продукта, количество, цена за единицу), и подсчитывает общую
выручку для каждого продукта. Итог должен быть сохранён в новом CSV файле.

Пример:
Из файла sales.csv нужно создать файл total_sales.csv, где для каждого продукта будет указана общая выручка.
"""
import csv
import os.path


def calk_sales(src_file, dst_file):
    if os.path.exists(src_file) and os.path.isfile(src_file):
        with open(src_file, 'r', newline='', encoding='utf-8') as f:
            rd = csv.DictReader(f)
            res = dict()
            for d in rd:
                sale = int(d['quantity']) * float(d['price'])
                name = d['product']
                res[name] = res.setdefault(name, 0) + sale
        with open(dst_file, 'w', newline='', encoding='utf-8') as f:
            er = csv.DictWriter(f, fieldnames=['product', 'total_sales'])
            er.writeheader()
            for product, total in res.items():
                er.writerow({'product': product, 'total_sales': total})

    else:
        print(f"Error: file {src_file} not found!")


if __name__ == '__main__':
    calk_sales('./datas/zad_4/sales.csv', './datas/zad_4/total_sales.csv')
