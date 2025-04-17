# Пользовательские исключения

class UserException(Exception):
    pass

class UserAgeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Возраст должен быть числом и больше нуля\nа вовсе не {type(self.value)}: {self.value}!"

class UserNameError(UserException):
    def __init__(self, value, lower, upper):
        self.value = value
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return f"Имя '{self.value}' не попадает в диапазон длин, от {self.lower} до {self.upper} символов!"

