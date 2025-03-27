"""
Задание №1.

Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_lenght(self):
        return 2 * math.pi * self.radius

    def get_square(self):
        return math.pi * (self.radius * self.radius)

    def __str__(self):
        return f"Circle: radius = {self.radius}"


t = Circle(12.3)
print(t)
print(f"Circle length = {t.get_lenght()}, circle.square = {t.get_square()}")
