"""
Задача 3. Тестирование класса с использованием doctest.

Напишите класс Rectangle, который управляет прямоугольником. Класс должен поддерживать следующие методы:
    ● set_dimensions(width, height): устанавливает ширину и высоту прямоугольника.
    ● get_area(): возвращает площадь прямоугольника.
    ● get_perimeter(): возвращает периметр прямоугольника.

Напишите 3 теста с помощью doctest.
"""
import doctest


class Rectangle:
    """ Класс прямоугольника.
    >>> Rectangle(12, 0)
    Traceback (most recent call last):
    ...
    ValueError: Некорректная высота для прямоугольника!

    >>> Rectangle('string', 10)
    Traceback (most recent call last):
    ...
    ValueError: Некорректная ширина для прямоугольника!

    >>> r = Rectangle(4, 2)
    >>> r.get_area()
    8

    >>> r = Rectangle(4, 2)
    >>> r.get_perimeter()
    12

    >>> r = Rectangle(4, 3)
    >>> r.set_dimension(-12, 10)
    Traceback (most recent call last):
    ...
    ValueError: Некорректная ширина для прямоугольника!

    >>> r = Rectangle(4, 3)
    >>> r.set_dimension(12, 0)
    Traceback (most recent call last):
    ...
    ValueError: Некорректная высота для прямоугольника!
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if isinstance(new_width, (int, float)) and new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Некорректная ширина для прямоугольника!")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if isinstance(new_height, (int, float)) and new_height > 0:
            self._height = new_height
        else:
            raise ValueError("Некорректная высота для прямоугольника!")

    def set_dimension(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        return f"Прямоугольник. Ширина = {self.width}. Высота = {self.height}."


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

