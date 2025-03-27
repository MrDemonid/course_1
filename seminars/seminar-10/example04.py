"""
Задание №4.

Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания. У сотрудника должен быть:
    ○ шестизначный идентификационный номер
    ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""
from example03 import Person


class Employee(Person):

    def __init__(self, idn, f_name, m_name, l_name, ages, hobby="No hobby"):
        self.idn = idn
        super().__init__(f_name, m_name, l_name, ages, hobby)

    def __get_level(self):
        n = self.idn
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s % 7

    def __str__(self):
        return f"{super().__str__()}, id = {self.idn}, level = {self.__get_level()}"


if __name__ == '__main__':
    p = Employee(1253721, "Иван", "Александрович", "Трубанов", 49, "прятки")
    s = Employee(6218193, "Елена", "Владимировна", "Трубанова", 48, "находилки")
    print(p)
    print(s)
