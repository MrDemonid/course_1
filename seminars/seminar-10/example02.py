"""
Задание №2.

Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""


class Rect:
    def __init__(self, width=-1, height=-1):
        if width == -1 and height == -1:
            width = 1
        self.width = height if width == -1 else width
        self.height = width if height == -1 else height

    def get_length(self):
        return self.width * self.width + self.height * self.height

    def get_square(self):
        return self.width * self.height

    def __str__(self):
        return f"Rect: width = {self.width}, height = {self.height}, length = {self.get_length()}, square = {self.get_square()}"


a = Rect(12)
b = Rect()
c = Rect(height=8)
d = Rect(4, 8)

print(a)
print(b)
print(c)
print(d)

