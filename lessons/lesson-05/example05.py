# Функция-генератор
from typing import Any, Generator


def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for n in factorial(5):
    print(n, end=' ')
print()


gen = iter(factorial(10))
print(next(gen))
print(next(gen))
print(next(gen))


def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)


for item in gen(10, 1):
    print(f'{item = }', end=', ')
print('\x08\x08')