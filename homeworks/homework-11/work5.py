"""
Задача 5. Абстрактный класс.

Вы работаете в компании, занимающейся разработкой программного обеспечения для
архитектурных проектов. Вам необходимо разработать программу для расчёта площади
различных геометрических фигур, таких как круги, прямоугольники и треугольники.

Задача

Создайте:
    ● класс Shape, который будет базовым классом для всех фигур и будет
        хранить пустой метод area, который наследники должны переопределить;
    ● класс Circle;
    ● класс Rectangle;
    ● класс Triangle.

Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод
для вычисления площади фигуры.

Дополнительно:
изучите информацию о работе с абстрактными классами. На основе этой информации сделайте
так, чтобы:
    1. Нельзя было создавать объекты класса Shape.
    2. Наследники класса Shape переопределяли его метод area, чтобы объекты этих
        классов можно было использовать.
"""
import math
from abc import abstractmethod, ABC


class Shape(ABC):
    """
    Абстрактный (ABC) класс фигуры.
    Содержит абстрактный метод вычисления площади фигуры,
    который должны переопределить потомки.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"{self.name}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Круг')
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{super().__str__()} [radius = {self.radius}]"


class Rectangle(Shape):
    def __init(self, width, height=None):
        super().__init__('Прямоугольник')
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{super().__str__()} [width = {self.width}, height = {self.height}]"


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__('Треугольник')
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __str__(self):
        return f"{super().__str__()} [a = {self.a}, b = {self.b}, {self.c}]"


# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8, 6)
# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()
# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
# Попытка создания экземпляра абстрактного класса Shape (должно вызвать ошибку)
try:
    shape = Shape() # Ожидается ошибка
except TypeError as e:
    print(f"Ошибка: {e}")
