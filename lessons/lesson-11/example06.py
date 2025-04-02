# Сравнение объектов

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Triangle [{self.a}, {self.b}, {self.c}]"

    def __eq__(self, other):
        this = sorted([self.a, self.b, self.c])
        outer = sorted([other.a, other.b, other.c])
        return this == outer


one = Triangle(3, 4, 5)
print(one)

two = Triangle(4, 3, 5)
print(two)

print(one == two)
print(one != two)

# Triangle [3, 4, 5]
# Triangle [4, 3, 5]
# True
# False
