"""
Задание №3.

Напишите класс для хранения информации о человеке:
    ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы:
    birthday для увеличения возраста на год,
    full_name для вывода полного ФИО
    и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст
"""

class Person:
    def __init__(self, f_name, m_name, l_name, ages, hobby="No hobby"):
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name
        self.ages = ages
        self.hobby = hobby

    def birthday(self):
        self.ages += 1

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_ages(self):
        return self.ages

    def get_hobby(self):
        return self.hobby

    def __str__(self):
        return f"Person: name = '{self.full_name()}', ages = {self.get_ages()}, hobby = {self.get_hobby()}"


if __name__ == '__main__':
    a = Person("Иван", "Александрович", "Трубанов", 49, "прятки")
    b = Person("Елена", "Владимировна", "Трубанова", 48, "находилки")
    b.birthday()
    print(a)
    print(b)
