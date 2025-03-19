"""
Задание №4.

Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.
"""
import time
from typing import Callable


def count(n: int = 1):
    def prepare(func: Callable):
        results = []
        def wrapper(*args, **kwargs):
            for _ in range(n):
                st = time.perf_counter_ns()
                func(*args, **kwargs)
                end = time.perf_counter_ns()
                results.append(end-st)
            return results
        return wrapper
    return prepare


@count(5)
def test_func(a, b, *, start = 1, end = 9):
    for i in range(start, end+1):
        a *= b
    return a


print(test_func(2, 2, end=18))
