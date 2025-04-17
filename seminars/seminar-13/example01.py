"""
Задание №1.

Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или вещественное число.
Обрабатывайте не числовые данные как исключения.
"""

def input_num(text):
    while True:
        n = input(text)
        try:
            return int(n)
        except ValueError:
            try:
                return float(n)
            except ValueError:
                pass


print(input_num("Введите число: "))
