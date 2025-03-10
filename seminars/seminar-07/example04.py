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
        ch_cnt = [min_name for _ in string.ascii_lowercase]         # повторы символов в имени
        while num_files > 0:
            name = "".join(sample(string.ascii_lowercase, randint(min_name, max_name), counts=ch_cnt)) + ext_name
            name = os.path.join(directory, name)
            try:
                f = open(name, 'wb')
            except IOError:
                print(f"  - error: file {name} is exists! Try now.")
            else:
                with f:
                    length = randint(min_length, max_length)
                    data = bytearray([randint(0, 255) for i in range(length)])
                    f.write(data)
                    num_files -= 1

    else:
        print("Error: bad parameters!")


if __name__ == '__main__':
    create_files('./datas/ex4', 'bin', num_files=4)
