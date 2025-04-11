"""
Задача 2. Класс с валидацией данных.

Создайте класс Person, который имеет атрибуты name, age, и email.
При установке значения атрибута name, оно должно начинаться с заглавной буквы.
При установке значения атрибута age, оно должно быть целым числом в диапазоне от 0 до 120.
При установке значения атрибута email, оно должно содержать символ @.
"""

from descs.fio import FIO
from descs.numb import RangeValidator
from descs.email import Email


class Person:
    name = FIO()
    age = RangeValidator(num_min=0, num_max=119)
    email = Email()

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Person(name = '{self.name}', age = {self.age}, email = {self.email})"


if __name__ == '__main__':
    p = Person("Иван Александрович", 49, 'ivan-gov@gmail.com')
    print(p)
    p.email = "askjd@sdfjk.com"
    t = Person("Ivan Gedesky", 49, "abra@yandex.com")
