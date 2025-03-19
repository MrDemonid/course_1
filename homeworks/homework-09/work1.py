"""
Задание 1. Как дела?

Вася совсем заскучал на работе и решил побаловаться с кодом проекта.
Он написал надоедливый декоратор, который при вызове декорируемой функции
спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то
вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после
такой выходки Васю чуть не уволили с работы.
Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.

Пример кода:
@how_are_you
def test():
print('<Тут что-то происходит...>')
test()

Результат:
Как дела? Хорошо.
А у меня не очень! Ладно, держи свою функцию.
<Тут что-то происходит...>
"""
from functools import wraps
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        input ("How are You? ")
        print("And mine is not so good! Okay, keep your function.")
        return func(*args, **kwargs)

    return wrapper


@how_are_you
def test(a, b):
    return a * b


@how_are_you
def test2(a, b, *, divider=2):
    return (a * b) // divider


print(f"{test(12, 6) = }")
print(f"{test2(12, 6) = }")
