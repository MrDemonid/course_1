# Конструктор экземпляра.


class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.health = 100


p1 = Person()
p2 = Person()

print(p1.max_up, p1.level, p1.health)
print(p2.max_up, p2.level, p2.health)
# print(Person.max_up, Person.level, Person.health)       # AttributeError: type object 'Person' has no attribute 'level'

Person.level = 200
print(p1.level, p2.level, Person.level)

# 3 1 100
# 3 1 100
# 1 1 200


