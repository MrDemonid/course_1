"""
Задача 4. Создание класса-фабрики для животных.

Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.

Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют
дополнительные атрибуты и методы:
    Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
    Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию
         глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
         Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
         Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
         В противном случае, рыба относится к категории "Средневодная рыба".
    Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего
         (Малявка, Обычный, Гигант) в зависимости от веса.
         Если вес объекта меньше 1, то он относится к категории "Малявка".
         Если вес объекта больше 200, то он относится к категории "Гигант".
         В противном случае, объект относится к категории "Обычный".

Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе
переданного типа и параметров.
Класс-фабрика должен иметь:
    метод create_animal, который принимает следующие аргументы:
        animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
        *args - переменное количество аргументов, представляющих параметры для конкретного
                типа животного.
    Количество и типы аргументов могут различаться в зависимости от типа животного.

Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.
Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с сообщением
'Недопустимый тип животного'.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not name is None and len(name) > 0:
            self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        super().__init__(name)

    def wing_length(self):
        """ Возвращает длину крыла птицы """
        return self.wingspan / 2

    def __str__(self):
        return f"{self.__class__.__name__} [name = {self.name}, wingspan = {self.wingspan}]"


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        if self.max_depth > 100:
            return "Глубоководная рыба"
        return "Средневодная рыба"

    def __str__(self):
        return f"{self.__class__.__name__} [name = {self.name}, max_depth = {self.max_depth}, category = {self.depth()}]"


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        if self.weight > 200:
            return "Гигант"
        return "Обычный"

    def __str__(self):
        return f"{self.__class__.__name__} [name = {self.name}, weight = {self.weight}, category = {self.category()}]"


class AnimalFactory:
    classes = {"Bird": Bird, "Fish": Fish, "Mammal": Mammal}

    @staticmethod
    def create_animal(animal_type, *args) -> Animal:
        if animal_type in AnimalFactory.classes:
            return AnimalFactory.classes[animal_type](*args)
        raise ValueError('Недопустимый тип животного')


if __name__ == '__main__':
    f = AnimalFactory.create_animal("Fish", "Гуппи", 30)
    print(f)
    b = AnimalFactory.create_animal("Bird", "Чиж", 14)
    print(b)
    m = AnimalFactory.create_animal("Mammal", "Хомяк", 0.6)
    print(m)
    t = AnimalFactory.create_animal("Dog", "Blue")  # ValueError: Недопустимый тип животного
