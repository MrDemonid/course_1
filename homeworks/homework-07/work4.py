"""
Задача 4. Поиск файлов по расширению.

Напишите функцию, которая находит и перечисляет все файлы с заданным расширением в указанном каталоге и всех его подкаталогах.
Функция должна принимать путь к каталогу и расширение файла.
"""

from pathlib import Path


def find_files(src_dir, ext_file):
    src_dir = Path(src_dir).resolve()
    if not ext_file.startswith('.'):
        ext_file = '.' + ext_file
    print(f"Start search files from {src_dir}")

    for fn in src_dir.rglob('*' + ext_file):
        print(f"  - found: {fn}")


if __name__ == '__main__':
    find_files('./dir-01', 'py')
