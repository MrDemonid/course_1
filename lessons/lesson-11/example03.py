# Дендер __doc__


class User:
    """ Документация класа User. """

    def __init__(self, name: str):
        """ Конструктор класс User. """
        self.name = name

    def simple_method(self):
        """ Пример метода. """
        self.name.capitalize()


u_1 = User('Спенглер')
print(f'{User.__doc__}')
print(f'{u_1.__doc__}')
print(f'{u_1.simple_method.__doc__}')

help(u_1)
