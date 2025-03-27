# Модификаторы доступа.

class Person:
    max_up = 3
    __max_level = 80

    def __init__(self, name, race='unknown', speed=150):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed

    def _check_speed(self):
        return self.level < self.__max_level

    def level_up(self):
        if self._check_speed():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p = Person("Ivan", "Human")
a = Person("Bert", "Alien", 200)

# print(p.__max_level)        # AttributeError: 'Person' object has no attribute '__max_level'
print(p._Person__max_level)     # __name -> _classname__name
print(p._speed, a._speed)

a._speed = 250
print(p._speed, a._speed)
