"""
Задача 2. Замедление кода.

В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.
Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
"""
from functools import wraps
from typing import Callable
import time


def wait(sec: int):
    def set_deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"wait {sec} seconds...")
            time.sleep(sec)
            return func(*args, **kwargs)
        return wrapper
    return set_deco


@wait(4)
def test_func():
    print("hello!")
    return "Ok"


print(f"Run {test_func.__name__}() =  {test_func()}")
