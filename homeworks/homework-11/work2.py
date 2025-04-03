"""
Задача 2. Магия.

Для одной игры необходимо реализовать механику магии, где при соединении
двух элементов получается новый.
У нас есть четыре базовых элемента:
    «Вода», «Воздух», «Огонь», «Земля».
Из них получаются новые:
    «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

Таблица преобразований:
    ● Вода + Воздух = Шторм;
    ● Вода + Огонь = Пар;
    ● Вода + Земля = Грязь;
    ● Воздух + Огонь = Молния;
    ● Воздух + Земля = Пыль;
    ● Огонь + Земля = Лава.

Напишите программу, которая реализует все эти элементы. Каждый элемент
необходимо организовать как отдельный класс. Если результат не определён,
то возвращается None.

Примечание: сложение объектов можно реализовывать через магический метод __add__,
вот пример использования:
class ExampleOne:
    def __add__(self, other):
        return ExampleTwo()

class ExampleTwo:
    answer = 'сложили два класса и вывели'

first_example = ExampleOne()
second_example = ExampleTwo()
result = first_example + second_example
print(result.answer)

Дополнительно: придумайте свой элемент (или элементы) и реализуйте его
взаимодействие с остальными.
"""


class Magic:
    """ Базовый класс магии """

    def __init__(self, name):
        self.name = name
        self.mixtures = dict()  # словарь возможных соединений компонентов

    def find_mixture(self, other):
        """ Поиск варианта соединения с заданным классом компонента """
        cls = other.__class__.__name__
        for k, v in self.mixtures.items():
            if k == cls:
                return v()
        return None

    def __add__(self, other):
        return self.find_mixture(other)

    def __str__(self):
        return f"{self.name}"


class Water(Magic):
    def __init__(self):
        super().__init__("Вода")
        self.mixtures = {'Fire': Steam, 'Air': Storm, 'Soil': Mud}


class Fire(Magic):
    def __init__(self):
        super().__init__("Огонь")
        self.mixtures = {'Water': Steam, 'Air': Bolt, 'Soil': Lava}


class Air(Magic):
    def __init__(self):
        super().__init__("Воздух")
        self.mixtures = {'Water': Storm, 'Fire': Bolt, 'Soil': Dust}


class Soil(Magic):
    def __init__(self):
        super().__init__("Земля")
        self.mixtures = {'Water': Mud, 'Fire': Lava, 'Air': Dust}


class Steam(Magic):
    def __init__(self):
        super().__init__('Пар')


class Storm(Magic):
    def __init__(self):
        super().__init__('Шторм')


class Mud(Magic):
    def __init__(self):
        super().__init__('Грязь')


class Bolt(Magic):
    def __init__(self):
        super().__init__("Молния")


class Dust(Magic):
    def __init__(self):
        super().__init__('Пыль')


class Lava(Magic):
    def __init__(self):
        super().__init__('Лава')


class Fog(Magic):
    def __init__(self):
        super().__init__('Туман')


if __name__ == '__main__':
    water = Water()
    fire = Fire()
    air = Air()
    soil = Soil()

    print(f"{water.name} + {fire.name} = {water + fire}")
    print(f"{water.name} + {air.name} = {air + water}")
    print(f"{water.name} + {soil.name} = {water + soil}")

    print(f"{fire.name} + {air.name} = {fire + air}")
    print(f"{fire.name} + {soil.name} = {fire + soil}")

    print(f"{air.name} + {soil.name} = {soil + air}")

