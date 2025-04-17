"""
Задание №4.

Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали
имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
"""


class User:
    def __init__(self, idn, name, level):
        self.idn = idn
        self.name = name
        self.level = level

    @property
    def idn(self):
        return self._idn

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @idn.setter
    def idn(self, value):
        if not value is None:
            self._idn = value
        else:
            raise ValueError(f"Значение идентификатора не может быть пустым!")

    @name.setter
    def name(self, value):
        if not value is None and len(value) > 0:
            self._name = value
        else:
            raise ValueError(f"Некорректное значение '{value}' для имени")

    @level.setter
    def level(self, value):
        if (not value is None) and isinstance(value, int):
            if 1 <= value <= 7:
                self._level = value
            else:
                raise ValueError(f"Значение уровня '{value}' выходит за диапазон 1..7")
        else:
            raise TypeError(f"Значение уровня должно быть целым числом!")

    def __str__(self):
        return f"Юзер [id = {self.idn}, name = {self.name}, level = {self.level}"


def new_user():
    """ Ввод данных для нового юзера. """
    while True:
        name = input("Введите имя: ")
        if 'exit' == name.lower():
            return None
        idn = input("Введите идентификатор: ")
        level = (input("Введите уровень доступа (1 - 7): "))
        try:
            return User(idn, name, int(level))
        except ValueError as e:
            print(f"Ошибка ввода: {e}\nПопробуйте снова.")
        except TypeError as e:
            print(f"Ошибка ввода type: {e}\nПопробуйте снова.")

def load_users():
    """ Чтение множества User из файла JSON"""
    pass



u = new_user()
