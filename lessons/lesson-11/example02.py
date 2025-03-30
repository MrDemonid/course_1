# Примеры использования __new__().

"""
1. Расширим функционал типа int, добавив ему имена.
"""
class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance

a = NamedInt(42, 'Переменная A')
b = NamedInt(73, 'Переменная B')
print(f'{a}    {a.name}    {type(a)}')
print(f'{b}    {b.name}    {type(b)}')
c = a + b
print(f'{c = }    {type(c) = }')

# Создал класс <class '__main__.NamedInt'>
# Создал класс <class '__main__.NamedInt'>
# 42    Переменная A    <class '__main__.NamedInt'>
# 73    Переменная B    <class '__main__.NamedInt'>
# c = 115    type(c) = <class 'int'>
print('--------------------------')


"""
2. Реализуем шаблон Singleton.
"""
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.name = name

a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')

# a.name = 'Первый'
# a is b = True
# a.name = 'Второй'
# b.name = 'Второй'
