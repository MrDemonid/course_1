"""
Задание №5.

Напишите функцию, которая ищет json файлы в указанной директории и
сохраняет их содержимое в виде одноимённых pickle файлов.
"""

import json
import pickle
from pathlib import Path


def conv_jsons_to_picle(directory):
    if Path(directory).is_dir():
        src_dir = Path(directory).resolve()
        for fn in src_dir.rglob('*.json'):
            print(f"  -- found: {fn}")
            with open(fn, 'r', encoding='utf-8') as f:
                res = json.load(f)
            name = Path(fn).with_suffix('.pickle')
            with open(name, 'wb') as f:
                print(f"  -- save to {name}")
                pickle.dump(res, f)
    else:
        print(f"Error: path '{directory}' not found")


if __name__ == '__main__':
    conv_jsons_to_picle('./datas')
