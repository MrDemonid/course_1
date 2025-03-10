"""
Задание №1
✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

import os
from random import randint
from random import uniform

def random_numbers(file_name, num_lines):
    with open(file_name, 'a', encoding='utf-8') as f:
        while num_lines:
            n = uniform(-1000.0, 1000.0)
            i = randint(-1000, 1000)
            f.write(f"{i}|{n:.2f}\n")
            num_lines -= 1


if __name__ == '__main__':
    random_numbers('./datas/numbers.txt', 50)

