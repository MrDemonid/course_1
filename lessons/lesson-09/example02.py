from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Bye')

print(hello('Alex'))
print(hello('Elly'))
print(bye('Alina'))
print(hello('Bert'))
print(bye('Neo'))

print('-----------------------')


def one_str(a: str) -> Callable[[str], str]:
    text = ''

    def two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text

    return two_str


hello = one_str('Hello')
bye = one_str('Good bye')
print(hello('Alex'))
print(hello('Elly'))
print(bye('Alina'))
print(hello('Bert'))
print(bye('Neo'))
