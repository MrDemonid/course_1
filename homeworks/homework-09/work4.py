"""
Задача 4. Кэширование для ускорения вычислений.

Создайте декоратор, который кэширует (сохраняет для дальнейшего использования) результаты вызова
функции и, при повторном вызове с теми же аргументами, возвращает сохранённый результат.
Примените его к рекурсивной функции вычисления чисел Фибоначчи.
В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
если такие аргументы уже использовались, должен вернуть сохранённый результат вместо запуска расчёта.
"""
from functools import wraps
from typing import Callable


def cache(func: Callable):
    _cache = dict()

    @wraps(func)
    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
            print(f"  -- to cache: {args}")
        return _cache[args]

    return wrapper


@cache
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


@cache
def reverse_string(s):
    """ Реверсивный разворот строки """
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


@cache
def NOD(a, b):
    """ Наибольший общий делитель """
    if b == 0:
        return a
    return NOD(b, a % b)


@cache
def power(base, exp):
    """ Быстрая версия возведения в степень для целочисленных чисел  """
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)



print(f"{factorial(5) = }")
print(f"{factorial(12) = }")
print(f"{factorial(9) = }")
print(f"{reverse_string('olleH')}")
print(f"{reverse_string('olleH')}")

print(f"{NOD(12, 6) = }")
print(f"{NOD(48, 24) = }")
print(f"{NOD(48, 12) = }")
print(f"{NOD(12, 6) = }")

print(f"{power(2, 8) = }")
print(f"{power(2, 4) = }")
print(f"{power(2, 6) = }")
