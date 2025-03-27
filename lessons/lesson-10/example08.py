# Множественное наследование.

class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"Person: '{self.name}', {self.year} years"


class Address:
    def __init__(self, city):
        self.city = city

    def __str__(self):
        return f"Address: '{self.city}'"


class Hero(Person, Address):
    def __init__(self, name, year, city):
        Person.__init__(self, name, year)
        Address.__init__(self, city)

    def __str__(self):
        return Person.__str__(self) + "\n" + Address.__str__(self)



p = Hero(name="Ivan", year=21, city="Moscow")
print(p)


