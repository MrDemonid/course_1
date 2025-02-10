# Все типы аргументов
def foo(a, /, b, *, c):
    print(a, b, c)


foo(1, 2, c=3)
foo(1, c=3, b=2)

# Дефолтные аргументы:
def foo(a, b, c):
    print(a, b, c)

foo(c=3, b=2, a=1)
foo(1, c=3, b=2)


# Только позиционные аргументы
def foo(a, b, c, /):
    print(a, b, c)

foo(1, 2, 3)


# Только ключевые аргументы
def foo(*, a, b, c):
    print(a, b, c)

foo(b=2, c=3, a=1)
