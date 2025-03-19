"""
Задание №3.

Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""
from random import randint
import json
import os.path
from typing import Callable

_LOG_NAME = './datas/ex3.json'


def log(func: Callable):
    def wrapper(*args, **kwargs):
        js = list()
        params = ', '.join(map(str, list(args)))
        kwparams = ', '.join(f"{key} = {value}" for key, value in dict(kwargs).items())
        if len(kwparams) > 0:
            params = ', '.join([params, kwparams])
        print(f"({params})")
        if os.path.isfile(_LOG_NAME):
            with open(_LOG_NAME, 'r', encoding='utf-8') as f:
                js = list(json.load(f))
        res = func(*args, **kwargs)
        print(res)
        js.append([{"params": f"({params})"}, {"result": res}])
        print(f"{js = }")
        with open(_LOG_NAME, 'w', encoding='utf-8') as f:
            json.dump(js, f, ensure_ascii=False, indent=2)

    return wrapper


@log
def test_func(a, b, *, key=2, start=12):
    print(f"test({a = }, {b = }, {key = }, {start = })")
    return (a * b + start) / key


print(test_func(randint(1, 10), randint(4, 15), start=randint(10, 30)))
