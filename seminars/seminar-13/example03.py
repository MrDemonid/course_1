"""
Задание №3.

Создайте класс с базовым исключением и дочерние классы исключения:
    - ошибка уровня.
    - ошибка доступа.
"""

class BaseSecurity(Exception):
    pass

class LevelError(BaseSecurity):
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return f"Уровня '{self.level}' недостаточно!"

class AccessError(BaseSecurity):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"Ошибка доступа: '{self.msg}'"

