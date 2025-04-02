# Сортировка объектов

from math import sqrt


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

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __lt__(self, other):
        return self.area() < other.area()

    def __repr__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"


data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 2, 4)]
res = sorted(data)
for t in res:
    print(f"{t}, with square = {t.area()}")

# Triangle [4, 2, 4], with square = 3.872983346207417
# Triangle [6, 2, 5], with square = 4.683748498798798
# Triangle [3, 4, 5], with square = 6.0
