"""
Задание №6.

Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.
"""
import json
import os
from functools import wraps
from random import randint
from typing import Callable


_LOG_NAME = './datas/ex6.json'


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
            json.dump(js, f, ensure_ascii=False, indent=4)

    return wrapper


def count(n: int = 1):
    def prepare(func: Callable):
        results = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return prepare


def run_func(func: Callable):
    @wraps(func)
    def wrapper(num: int, count: int):
        print(f"-- check params ({num}, {count})")
        if num < 1 or num > 100:
            num = randint(1, 100)
        if count < 1 or count > 10:
            count = randint(1, 10)
        func(num, count)

    return wrapper


@count(3)
@run_func
@log
def bulls_and_cows(num: int, count: int):
    for _ in range(count):
        n = int(input("-- my number (1-100)?: "))
        if n == num:
            return "You win!"
        if n > num:
            print("  -- my number is less!")
        else:
            print("  -- my number is great!")
    return f"You loss! number is {num}"


bulls_and_cows(0, 9)
