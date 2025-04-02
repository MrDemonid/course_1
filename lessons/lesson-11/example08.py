# Hash

from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f"Triangle [{self._a}, {self._b}, {self._c}]"

    def __eq__(self, other):
        this = sorted([self._a, self._b, self._c])
        outer = sorted([other._a, other._b, other._c])
        return this == outer

    def area(self):
        p = (self._a + self._b + self._c) / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    def __lt__(self, other):
        return self.area() < other.area()

    def __repr__(self):
        return f"Triangle({self._a}, {self._b}, {self._c})"

    def __hash__(self):
        return hash((self._a, self._b, self._c))


# Теперь экземпляры Triangle стали неизменяемыми и мы можем использовать их в Set:
data = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 2, 4)}
res = sorted(data)
for t in res:
    print(f"{t}, with square = {t.area()}")
