"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.

Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""

import os
import string
from random import sample, randint


def create_files(directory, ext_name: str, *, min_name=6, max_name=30, min_length=256, max_length=4096, num_files=42):
    if not ext_name.startswith('.'):
        ext_name = '.' + ext_name
    if min_name > max_name:
        min_name, max_name = max_name, min_name
    if min_length > max_length:
        min_length, max_length = max_length, min_length
    if os.path.isdir(directory) and not ext_name is None and min_name > 0 and min_length > 0:
        # готовим уникальные имена файлов
        alph = [ch for ch in string.ascii_lowercase]
        ch_cnt = [min_name for _ in string.ascii_lowercase]         # повторы символов в имени
        names = []
        while num_files > 0:
            name = "".join(sample(alph, randint(min_name, max_name), counts=ch_cnt)) + ext_name
            name = os.path.join(directory, name)
            if not name in names:
                names.append(f"{name}")
                num_files -= 1
        # создаем файлы и пишем в них случайные данные
        for name in names:
            length = randint(min_length, max_length)
            with open(name, 'wb') as f:
                data = bytearray([randint(0, 255) for i in range(length)])
                f.write(data)

    else:
        print("Error: bad parameters!")


if __name__ == '__main__':
    create_files('./datas/ex4', 'bin')
