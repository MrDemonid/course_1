"""
Задание №6.

Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def show_specify(self):
        print("Animal: no specify for abstract class!")

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Animal: name = {self.name}"


class Fish(Animal):
    def __init__(self, name, deep):
        self.deep = deep
        super().__init__(name)

    def show_specify(self):
        print(f"Fish: deep = {self.deep}")

    def __str__(self):
        return f"Fish: name = {self.name}, deep = {self.deep}"


class Bird(Animal):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    def show_specify(self):
        print(f"Bird: height = {self.height}")

    def __str__(self):
        return f"Bird: name = {self.name}, height = {self.height}"


if __name__ == '__main__':
    a = Animal("Леший")
    f = Fish("Окунь", "средне")
    b = Bird("Чиж", "низко")

    a.show_specify()
    f.show_specify()
    b.show_specify()
    print(a)
    print(f)
    print(b)
