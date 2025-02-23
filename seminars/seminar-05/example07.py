"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел, начиная с числа 2.
✔ Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».
"""
from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False

    n = sqrt(number)
    for divider in range(3, int(n), 2):
        if number % divider == 0:
            return False
    return True


#
# функция-генератор простых чисел
#
def prime(n):
    for x in range(2, n):
        if x == 2 or x == 3:
            yield x
            continue
        if is_prime(x):
            yield x
            continue


gen = prime(100)
for i in gen:
    print(i, end=', ')
print('\x08\x08')
