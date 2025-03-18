from typing import Callable


# Переменные в декораторе. На примере кэширования результатов вызова функции.

def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper


@cache
def factorial(n: int) -> int:
    print(f'-- calc for {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(5) = }')
print(f'{factorial(8) = }')
print(f'{factorial(5) = }')
print(f'{factorial(10) = }')
print(f'{factorial(5) = }')
print(f'{factorial(10) = }')
