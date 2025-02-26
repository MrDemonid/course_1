from random import randint

__all__ = ['rnd', '_SIZE']  # ограничиваем экспорт для импорта через '*'

_SIZE = 100

def foo(a, b):
    return randint(a, b)


def rnd(a, b) -> str:
    res = f"Random({a}, {b}) = {foo(a, b)}"
    return res

