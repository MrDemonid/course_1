"""
Задача 3. Удаление старых файлов.

Напишите скрипт, удаляющий файлы в указанном каталоге, которые не
изменялись более заданного количества дней.
Скрипт должен принимать путь к каталогу и количество дней.
"""

import os
import time


def delete_old_files(src_dir, num_days):
    src_dir = os.path.abspath(src_dir)
    print(f"Start delete older files from {src_dir}")
    last_time = time.time() - (num_days * 24 * 60 * 60)
    for cur_dir, dirs, files in os.walk(src_dir):
        for fn in files:
            full_name = os.path.join(cur_dir, fn)
            if os.path.getmtime(full_name) < last_time:
                print(f'  - delete file {os.path.join(cur_dir, fn)}')
                os.remove(full_name)


if __name__ == '__main__':
    delete_old_files('./dir-03', 4)
