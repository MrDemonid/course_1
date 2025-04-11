"""
Задание №1.
Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
"""
from functools import reduce


class Cache:
    """ Класс кэширования значения и результата для функции с одним параметром """

    def __init__(self, size):
        self.cache = dict()
        self.order = []
        self.size = size if 0 < size < 1000 else 500

    def put(self, key, value):
        if not key in self.cache:
            self.cache[key] = value
            if len(self.order) >= self.size:
                older = self.order.pop(0)
                del self.cache[older]
            self.order.append(key)

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None

    def get_cache(self):
        return f"{self.cache}"


class Factorial:

    def __init__(self, cache_size: int):
        self.cache = dict()
        self.size = cache_size
        self.cache = Cache(cache_size)

    def __call__(self, n):
        res = self.cache.get(n)
        if res is None:
            res = reduce(lambda x, y: x * y, range(1, n + 1), 1)
            self.cache.put(n, res)
            print("put to cache: ", end='  ')
        return res
        # result = 1
        # for i in range(2, n+1):
        #     result *= i
        # return result

    def __str__(self):
        return f"Cache: {self.cache.get_cache()}"


if __name__ == '__main__':
    f = Factorial(10)
    print(f(5))
    print(f(10))
    print(f(8))
    print(f(10))
    print(f(5))
    print(f)
