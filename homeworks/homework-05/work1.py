"""
Задание 1. Квадраты чисел
Пользователь вводит число N. Напишите программу, которая генерирует
последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
далее). Реализацию напишите двумя способами: функция-генератор и
генераторное выражение.
"""
from typing import Iterator


def func_quadratic(n: int) -> Iterator[int]:
    for n in range(1, n + 1):
        yield n * n


number = int(input("Enter the number: "))
for i in func_quadratic(number):
    print(i, end=', ')
print('\x08\x08')

gen = (n * n for n in range(1, number + 1))

for i in gen:
    print(i, end=', ')
print('\x08\x08')
