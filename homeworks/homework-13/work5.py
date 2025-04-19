"""
Задача 5. Валидатор Пользовательских Данных.

Создайте класс User, который содержит атрибуты name, email, и age.
Необходимо убедиться, что:
    ● Имя состоит из хотя бы двух слов, каждое из которых начинается с заглавной буквы.
    ● Электронная почта содержит символ @ и точку . после @.
    ● Возраст — это положительное целое число, не меньше 0 и не больше 120.

Создайте пользовательские исключения для каждой из этих проверок:
    ● NameError: Если имя не соответствует формату.
    ● EmailError: Если электронная почта не соответствует формату.
    ● AgeError: Если возраст вне допустимого диапазона.
"""


class NameError(Exception):
    def __init__(self, msg):
        super().__init__(f"Неверное имя пользователя: {msg}")


class EmailError(Exception):
    def __init__(self, msg):
        super().__init__(f"Неверный e-mail: {msg}")


class AgeError(Exception):
    def __init__(self, msg):
        super().__init__(f"Некорректный возраст: {msg}")


class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise AgeError("Возраст должен быть целочисленным")
        if 0 <= age <= 120:
            self._age = age
        else:
            raise AgeError("Возраст должен быть в диапазоне 0-120 лет")

    @name.setter
    def name(self, name):
        parts = name.strip().split()
        if len(parts) < 2:
            raise NameError("Имя должно состоять хотя бы из двух слов")
        for part in parts:
            if not (part.isalpha() and part[0].isupper() and part[1:].islower()):
                raise NameError("Каждая часть ФИО должна начинаться с заглавной буквы и содержать только буквы!")
        self._name = " ".join(parts)

    @email.setter
    def email(self, value):
        t = value.split("@")
        if len(t) != 2 or not "." in t[-1]:
            raise EmailError("Почта должна содержать символ '@' и точку после него")
        self._email = value

    def __str__(self):
        return f"User [name = {self.name}, age = {self.age}, email = {self.email}]"


if __name__ == '__main__':
    try:
        user = User(name="John Doe", email="john.doe@example.com", age=25)
        print(f"User created: {user.name}, {user.email}, {user.age}")

    except (NameError, AgeError, EmailError) as e:
        print(e)
