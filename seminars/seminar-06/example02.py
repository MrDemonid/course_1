"""
Задание №2
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
from random import randint

IS_DEBUG = False

def bulls_and_cows(start, stop, count):
    num = randint(start, stop)
    if IS_DEBUG:
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


if __name__ == '__main__':
    IS_DEBUG = True
    print(bulls_and_cows(1, 9, 3))
