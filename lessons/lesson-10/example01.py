class Person:
    max_up = 3

p = Person()
print(p.max_up)


p1 = Person()
p2 = Person()
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
p1.max_up = 12
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
Person.max_up = 42
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

# Person.max_up = 3, p1.max_up = 3, p2.max_up = 3
# Person.max_up = 3, p1.max_up = 12, p2.max_up = 3
# Person.max_up = 42, p1.max_up = 12, p2.max_up = 42
