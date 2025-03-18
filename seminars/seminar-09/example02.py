"""
Задание №2.

Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""
import random
from typing import Callable


def run_func(func: Callable):
    def wrapper(num: int, count: int):
        if num < 1 or num > 100:
            num = random.randint(1, 100)
        if count < 1 or count > 10:
            count = random.randint(1, 10)
        func(num, count)

    return wrapper


@run_func
def bulls_and_cows(num: int, count: int):
    n = -num
    for _ in range(count):
        n = int(input("-- my number (1-100)?: "))
        if n == num:
            print("You win!")
            return
        if n > num:
            print("  -- my number is less!")
        else:
            print("  -- my number is great!")
    print(f"You loss! number is {num}")


# run_func(bulls_and_cows)(1000, 0)
bulls_and_cows(1000, 0)

