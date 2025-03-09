"""
Задача 2. Создание архива каталога.

Напишите скрипт, который создает архив каталога в формате .zip.
Скрипт должен принимать путь к исходному каталогу и путь к целевому архиву.
Архив должен включать все файлы и подпапки исходного каталога.
"""

from pathlib import Path
import zipfile


def archive_directory(src_dir, arch_name):
    # делаем путь абсолютным
    src_dir = Path(src_dir).resolve()
    print(f"Start zipped from {src_dir}")
    with zipfile.ZipFile(arch_name, 'w', zipfile.ZIP_DEFLATED) as f:
        for fn in src_dir.rglob('*'):
            if fn.is_file():
                print(f"  - add to {fn}")
                rel_path = fn.relative_to(src_dir)
                f.write(fn, rel_path)


if __name__ == '__main__':
    archive_directory('./dir-01', './dir-02/reserved.zip')
    # archive_directory(Path(Path.cwd() / 'dir-01'), './dir-02/reserved.zip')


# Вариант рабочий, но PyCharm ругается на возможные проблемы с типами данных в os.path.join()
#
# def archive_directory(src_dir, arch_name):
#     src_dir = os.path.abspath(src_dir)
#     print(f"Start zipped from {src_dir}")
#     with zipfile.ZipFile(arch_name, 'w', zipfile.ZIP_DEFLATED) as f:
#         for dir_path, dirs_name, files_name in os.walk(src_dir):
#             for fn in files_name:
#                 file_name: str = os.path.join(dir_path, fn)
#                 f.write(file_name, os.path.relpath(file_name, src_dir))
