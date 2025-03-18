from typing import Callable


# Множественное декорирование

def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Старт A')
        print(f'  -- запуск {func.__name__}')
        res = func(*args, **kwargs)
        print(f'  -- завершение A')
        return res

    print('Возвращаем декоратор A')
    return wrapper_a


def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Старт B')
        print(f'  -- запуск {func.__name__}')
        res = func(*args, **kwargs)
        print(f'  -- завершение B')
        return res

    print('Возвращаем декоратор B')
    return wrapper_b


def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Старт C')
        print(f'  -- запуск {func.__name__}')
        res = func(*args, **kwargs)
        print(f'  -- завершение C')
        return res

    print('Возвращаем декоратор C')
    return wrapper_c


@deco_c
@deco_b
@deco_a
def main():
    print('Старт основной функции')


main()
