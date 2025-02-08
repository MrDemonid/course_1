"""
Задача 2. Поиск наибольшего числа в списке.
    Напишите программу, которая принимает список чисел через строку и
возвращает наибольшее число в этом списке.
"""
from xmlrpc.client import MAXINT

inp = "123 2 3 4 -5 6 3 68 3 8 2 6".split()

# Вариант 1
print(int(max(inp, key=int)))

# Вариант 2
# Проверка строки на отрицательное целое
def is_signed_integer(s):
    try:
        return s.lstrip("+-").isdigit() and int(s) == float(s)
    except ValueError:
        return False

max_elem = -MAXINT
for elem in inp:
    if is_signed_integer(elem):
        n = int(elem)
        if n > max_elem:
            max_elem = n
print(max_elem)
