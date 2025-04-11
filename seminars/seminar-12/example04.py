"""
Задание №4.
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину прямоугольника и встройте
контроль недопустимых значений (отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if (not value is None) and value > 0:
            self._width = value
        else:
            raise ValueError(f"Ширина должна быть больше нуля!")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not value is None and value > 0:
            self._height = value
        else:
            raise ValueError(f"Высота должна быть больше нуля!")

    def __str__(self):
        return f"Прямоугольник [ширина = {self._width}, высота = {self._height}, площадь = {self.area()}]"


if __name__ == '__main__':
    r = Rectangle(12, 18)
    r.width = 20
    print(r)
    r.height = 10
    print(r)



