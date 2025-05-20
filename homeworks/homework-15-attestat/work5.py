"""
Задача 5. Запуск из командной строки.

Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит: имя файла без расширения или название каталога, расширение,
если это файл, флаг каталога, название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""
import argparse
import logging
from collections import namedtuple
from pathlib import Path


# формат сообщений в лог
FORMAT = "{levelname} [{asctime}]: {msg}"


def is_directory(path):
    return not path is None and len(path) > 0 and Path(path).is_dir()

def get_absolute_path(path):
    return Path(path).resolve()


def get_info_directory(path, log):
    s = f"Scan directory: '{get_absolute_path(args.directory)}'"
    print(s)
    log.info(s)
    info = []
    src_dir = Path(path).resolve()
    for elem in src_dir.rglob("*"):
        is_dir = elem.is_dir()
        name = elem.name if is_dir else elem.stem
        ext = '' if is_dir else elem.suffix.lstrip('.')
        o = ObjInfo(name, ext, is_dir, elem.parent.name)
        log.info(f"name = '{o.name}' | ext = '{o.ext}' | dir = '{o.is_dir}' | parent = '{o.parent}'")
        info.append(o)
    return info


if __name__ == '__main__':
    # Получаем аргументы командной строки
    p = argparse.ArgumentParser("Directory info's parser.")
    p.add_argument("directory", type=str, help="Path to directory")
    args = p.parse_args()

    # Инициализируем файл лога
    logging.basicConfig(filename='work5.log', filemode='a', encoding='utf-8',
                        format=FORMAT,
                        style='{',
                        level=logging.INFO)
    log = logging.getLogger(__name__)

    # Создаем класс для хранения информации об объектах каталога
    ObjInfo = namedtuple("ObjInfo", "name ext is_dir parent")

    # собственно делаем задание
    if is_directory(args.directory):
        # собираем информацию о каталоге
        lst = get_info_directory(args.directory, log)
        print("Done!\nResults:\n", *(''+ l.__repr__() +'\n' for l in lst))
    else:
        # неверный параметр, выводим справку и уходим
        p.print_help()
