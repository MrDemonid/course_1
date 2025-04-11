"""
Задача 2. Класс с валидацией данных.

Создайте класс Person, который имеет атрибуты name, age, и email.
При установке значения атрибута name, оно должно начинаться с заглавной буквы.
При установке значения атрибута age, оно должно быть целым числом в диапазоне от 0 до 120.
При установке значения атрибута email, оно должно содержать символ @.
"""

class FIO:
    """ Дескриптор для ФИО """

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"Значение '{value}' должно быть строкой!")

        parts = value.strip().split()
        if not (1 <= len(parts) <= 3):
            raise ValueError("ФИО должно содержать от 1 до 3 слов!")

        for part in parts:
            if not (part.isalpha() and part[0].isupper() and part[1:].islower()):
                raise ValueError(
                    "Каждая часть ФИО должна начинаться с заглавной буквы и содержать только буквы кириллицы!")
        setattr(instance, self.name, value)


class Number:
    """ Дескриптор для целых чисел из заданного диапазона """

    def __init__(self, num_min: int = None, num_max: int = None):
        self._min = num_min
        self._max = num_max

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение '{value}' должно быть целочисленным!")
        if not self._min is None and value < self._min:
            raise ValueError(f"Значение '{value}' должно быть больше или равно '{self._min}'")
        if not self._max is None and value > self._max:
            raise ValueError(f"Значение '{value}' должно быть меньше или равно '{self._max}'")
        setattr(instance, self.name, value)

class Email:
    """ Дескриптор для мыла """

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"Значение '{value}' должно быть строкой!")
        if not "@" in value and not "." in value.split("@")[-1]:
            raise ValueError(f"Значение '{value}' не является электронной почтой!")
        setattr(instance, self.name, value)
