"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
import os

from example04 import create_files

__DEF_DIRECTORY = './datas/ex6'


def create_files_multi_ext_safe(directory, ext_name: dict[str:int], *, min_n=6, max_n=30, min_len=256, max_len=4096):
    if directory is None or not os.path.isdir(directory):
        directory = __DEF_DIRECTORY
    try:
        os.mkdir(directory)
        # os.chdir(directory)
    except FileExistsError:
        print('  - directory is already exists!')
        # os.chdir(directory)
    for k, v in ext_name.items():
        create_files(directory, k, min_name=min_n, max_name=max_n, min_length=min_len, max_length=max_len, num_files=v)


if __name__ == '__main__':
    create_files_multi_ext_safe(None, {'bin': 4, 'hex': 3, 'com': 2})

