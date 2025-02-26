#
# Тест директивы __all__ в импортируемом модуле
#
from module3 import *


def foo(a, b):
    """Функция не должна переопределить аналогичную в module3.py"""
    return f"This is my foo({a}, {b})"


print(_SIZE)
print(rnd(1, 100))
print(foo(1, 6))
