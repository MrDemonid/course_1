"""
Задание №5.

Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длину и ширину.
При вычитании не допускайте отрицательных значений
"""

# !!! Задача не имеет смысла, поскольку нельзя складывать и вычитать
# !!! периметры, не корректируя длины сторон.
#
# Странно, что преподаватель не заметил этого.

class Rect:
    def __init__(self, width=-1, height=-1):
        if width == -1 and height == -1:
            width = 1
        self.width = height if width == -1 else width
        self.height = width if height == -1 else height

    def get_perimeter(self):
        return (self.width + self.height) * 2


    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rect: width = {self.width}, height = {self.height}, length = {self.get_perimeter()}, square = {self.get_area()}"

    def __add__(self, other):
        p = self.get_perimeter() + other.get_perimeter()
        r = Rect()
        r.s
