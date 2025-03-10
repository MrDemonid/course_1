"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

from example04 import create_files


def create_files_multi_ext(directory, ext_name: dict[str:int], *, min_n=6, max_n=30, min_len=256, max_len=4096):
    for k, v in ext_name.items():
        create_files(directory, k, min_name=min_n, max_name=max_n, min_length=min_len, max_length=max_len, num_files=v)


if __name__ == '__main__':
    create_files_multi_ext('./datas/ex5', {'bin': 4, 'hex': 3, 'com': 2})

