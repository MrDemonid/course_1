# Декоратор @property. Геттеры, сеттеры и делеттеры.

class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value is None:
            self._name = value

    @name.deleter
    def name(self):
        self._name = "----"


u = User("Ivan")
u.name = "Andrey"
print(u.name)
del u.name
print(u.name)

        