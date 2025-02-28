"""
Задание №3
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
� Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""
from sys import argv
from random import randint

__all__ = ['bulls_and_cows']

__IS_DEBUG = False


def _do_bulls_and_cows(start, stop, count):
    num = randint(start, stop)
    if __IS_DEBUG:
        print("-- random number: ", num)
    while count > 0:
        n = int(input(f"Enter the number at {start} to {stop}; remainder count = {count}: "))
        if n == num:
            return True
        if n < num:
            print("- less")
        else:
            print("- great")
        count -= 1
    return False


_def_params = [1, 100, 5]


def _get_args():
    """
    Получаем с параметров командной строки значения для функции bull_and_cows()
    Если их мало, то возвращаем дефолтные.
    """
    n = [int(p) for p in argv[1:] if
         p.isdigit()]  # мы пропускаем имя файла, поэтому isdigit() - это просто подстраховка для некорректных параметров
    while len(n) < 3:
        n.append(_def_params[len(n)])
    return n


def bulls_and_cows():
    """ Импортируемая функция, использующая параметры командной строки """
    start, stop, count, *_ = _get_args()
    if start < stop:
        print(_do_bulls_and_cows(start, stop, count))
    else:
        print("Start and End numbers is bad!")


if __name__ == '__main__':
    __IS_DEBUG = True
    bulls_and_cows()
