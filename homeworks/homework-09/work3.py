"""
Задача 3. Счётчик.

Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
Для решения задачи нельзя использовать операторы global и nonlocal.

Пример: Из файла products.json нужно создать products.csv.
"""
from functools import wraps
from typing import Callable
from random import randint


def counter(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f"The function '{func.__name__}()' was called {wrapper.count} times")
        return res
    wrapper.count = 0
    return wrapper


@counter
def test_func(a, b):
    return a * b

print(f"{test_func(randint(1, 5), randint(2, 9))}")
print(f"{test_func(randint(1, 5), randint(2, 9))}")
print(f"{test_func(randint(1, 5), randint(2, 9))}")
print(f"{test_func(randint(1, 5), randint(2, 9))}")

