# Любое количество позиционных параметров
def foo(*args):
    print(sum(args))


foo(1, 2, 3, 4)
foo(*[1, 2, 3, 4])


# Любое количество ключевых параметров
def foo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")


foo(химия=5, алгебра=4, физика=5)
foo(**{'химия': 4, 'алгебра': 5, 'физика': 3})


# Любое количество ключевых параметров
def foo(*args, **kwargs):
    print(sum(args))
    print(kwargs)

foo(1, 2, 3, 4, химия=5, алгебра=4)
