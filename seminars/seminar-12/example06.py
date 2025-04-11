"""
Задание №6.
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
"""


class RangeValidator:
    """ Дескриптор для чисел из заданного диапазона """

    def __init__(self, *, num_min: int = None, num_max: int = None, value_type=(int,)):
        """
        Инициализация дескриптора:
            num_min - минимальное значение числа (если задано)
            num_max - максимальное значение числа (если задано)
            value_type - кортеж возможных типов числа, по умолчанию - целочисленное

            Если значения диапазонов не заданы, то контролируется просто тип присваиваемого значения.
        """
        self._min = num_min
        self._max = num_max
        self._type = value_type

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self  # обращение к дескриптору через класс
        return getattr(instance, self.name)  # обращение через экземпляр класса

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError(
                f"Значение '{value}' должно быть одного из типов: '{", ".join(t.__name__ for t in self._type)}'!")
        if not self._min is None and value < self._min:
            raise ValueError(f"Значение '{value}' для {self.name} должно быть больше или равно '{self._min}'")
        if not self._max is None and value > self._max:
            raise ValueError(f"Значение '{value}' для {self.name} должно быть меньше или равно '{self._max}'")
        setattr(instance, self.name, value)


class Rectangle:
    width = RangeValidator(num_min=0, value_type=(int, float))
    height = RangeValidator(num_min=0, value_type=(int, float))

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def __str__(self):
        return f"Прямоугольник [ширина = {self.width}, высота = {self.height}, площадь = {self.area()}]"


if __name__ == '__main__':
    r = Rectangle(12, 18)
    r.width = 20
    print(r)
    r.height = 0.2
    print(r)
