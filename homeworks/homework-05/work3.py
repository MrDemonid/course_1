"""
Задача 3. Генератор последовательности чисел Фибоначчи.

Напишите генераторную функцию fibonacci(n), которая принимает на вход
одно целое число n и возвращает последовательность первых n чисел
Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
число является суммой двух предыдущих, начиная с 0 и 1.
"""
from typing import Iterator


def fibonacci(top: int) -> Iterator[int]:
    p, n = 0, 1
    for _ in range(top):
        yield p
        p, n = n, n + p


for number in fibonacci(20):
    print(number, end=', ')
print('\x08\x08')

