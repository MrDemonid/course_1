# Динамическое изменение класса и его экземпляров.


class Person:
    max_up = 3


p1 = Person()
p2 = Person()

Person.level = 1
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

p1.health = 100
print(f'{p1.health = }')
print(f'{p2.health = }')        # AttributeError: 'Person' object has no attribute 'health'
print(f'{Person.health = }')    # AttributeError: type object 'Person' has no attribute 'health'
