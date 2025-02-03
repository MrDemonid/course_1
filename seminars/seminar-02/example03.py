"""
Задание №4
✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

import decimal

decimal.getcontext().prec = 42  # устанавливаем точность

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')


def area(diameter) -> decimal:
    d = decimal.Decimal(diameter)
    return pi * ((d / 2) ** 2)


def circle_len(diameter):
    return pi * decimal.Decimal(diameter)


diameter = float(input("Введите диаметр: "))
s = area(diameter)
l = circle_len(diameter)
print(f"Радиус  : {diameter / 2}, площадь окружности: {s}, длина окружности: {l}")
# и выводим разметку, для сравнения, что точность работает
print(f"Разметка: {diameter / 2}, площадь окружности: {'*' * 43}, длина окружности: {'@' * 43}")
