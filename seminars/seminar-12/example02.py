"""
Задание №2.
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""
import copy
from functools import reduce
import json


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
        return copy.deepcopy(self.cache)    # возвращаем копию, чтобы извне не поменяли


class Factorial:

    def __init__(self, filename, cache_size: int):
        self.filename = filename
        self.cache = dict()
        self.size = cache_size
        self.cache = Cache(cache_size)

    def __call__(self, n):
        res = self.cache.get(n)
        if res is None:
            res = reduce(lambda x, y: x * y, range(1, n + 1), 1)
            self.cache.put(n, res)
        return res
        # result = 1
        # for i in range(2, n+1):
        #     result *= i
        # return result

    def __str__(self):
        return f"Cache: {self.cache.get_cache()}"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, 'w') as f:
            json.dump(self.cache.get_cache(), f, indent=2)



if __name__ == '__main__':
    factorial = Factorial('factorial.json', 10)
    with factorial as f:
        print(f"{f(5) = }")
        print(f"{f(10) = }")
        print(f"{f(8) = }")
        print(f"{f(10) = }")
        print(f"{f(5) = }")
        print(f"{f(12) = }")
        print(f)

