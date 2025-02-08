"""
Задание №3
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""
import re

# Проверка строки на содержание вещественного числа
def is_float(s):
    try:
        num = float(s)
        return '.' in s or 'e' in s or num != int(num)
    except ValueError:
        return False

# Проверка строки на отрицательное целое
def is_signed_integer(s):
    try:
        return s.lstrip("+-").isdigit() and int(s) == float(s)
    except ValueError:
        return False



inp = ["1", "1.2", "True", "-5", "Text", "-5.0", "text"]


for item in inp:
    print("Значение: ", item, end=",    ")

    if item.isdigit():
        print("Целое положительное: ", int(item))
    elif is_signed_integer(item):
        print("Целочисленное отрицательное: ", int(item))
    elif is_float(item):
        print("Вещественное: ", float(item))
    elif item.islower():
        print("Остальные случаи: ", item)
    else:
        print("В строке есть заглавные буквы: ", item)

