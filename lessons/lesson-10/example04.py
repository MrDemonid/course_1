# Методы класса


class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p = Person("Ivan", "Human")
a = Person("Bert", "Alien")

print(p.level, a.level)

p.level_up()

print(p.level, a.level)

p.change_health(a, 50)
print(p.health, a.health)

# 1 1
# 2 1
# 150 50
