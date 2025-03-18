from functools import cache


# Декоратор cache. По сути то, что делали в 6-м примере - кеширование данных.

@cache
def factorial(n: int) -> int:
    print(f'-- factorial {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(5) = }')
print(f'{factorial(15) = }')
print(f'{factorial(5) = }')
print(f'{factorial(10) = }')
print(f'{factorial(5) = }')
print(f'{factorial(10) = }')
