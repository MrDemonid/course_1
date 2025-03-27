"""
Задание №5.
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""


class Fish:
    def __init__(self, name, deep):
        self.name = name
        self.deep = deep

    def get_specify(self):
        print(f"deep: {self.deep}")

    def __str__(self):
        return f"Fish: name = {self.name}, deep = {self.deep}"


class Bird:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def get_specify(self):
        print(f"Bird: height = {self.height}")

    def __str__(self):
        return f"Bird: name = {self.name}, height = {self.height}"


if __name__ == '__main__':
    f = Fish("Карась", "глубоко")
    b = Bird("Синица", "низко")
    print(f)
    print(b)
