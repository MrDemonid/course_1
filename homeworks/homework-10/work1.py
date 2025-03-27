"""
Задание 1. Отцы, матери и дети.
Вася совсем заскучал на работе и решил побаловаться с кодом проекта.
Реализуйте два класса: «Родитель» и «Ребёнок».
У родителя есть:
    ● имя,
    ● возраст,
    ● список детей.
И он может:
    ● сообщить информацию о себе,
    ● успокоить ребёнка,
    ● покормить ребёнка.
У ребёнка есть:
    ● имя,
    ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
    ● состояние спокойствия,
    ● состояние голода.
Реализация состояний — на ваше усмотрение.
Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.
"""
import copy


class Children:
    _CHILD_CALM = 1  # флаг спокойствия ребенка
    _CHILD_HUNGRY = 2  # флаг сытости ребенка

    def __init__(self, name, ages):
        self.name = name
        self.ages = ages
        self.__status = self._CHILD_CALM | self._CHILD_HUNGRY  # неспокоен и голоден

    def is_calm(self) -> bool:
        return self.__status & self._CHILD_CALM > 0

    def is_hungry(self) -> bool:
        return self.__status & self._CHILD_HUNGRY > 0

    def calm(self, status: bool):
        self.__set_status(status, self._CHILD_CALM)

    def hungry(self, status: bool):
        self.__set_status(status, self._CHILD_HUNGRY)

    def __set_status(self, status, flag):
        if status:
            self.__status |= flag
        else:
            self.__status = (self.__status & (~flag))

    def __str__(self):
        return f"Children: name = {self.name}, ages = {self.ages}, calm = {self.is_calm()}, hungry = {self.is_hungry()}"


class Parent:
    def __init__(self, name, ages):
        self.name = name
        self.ages = ages
        self.children: list[Children] = list()

    def get_name(self):
        return self.name

    def get_ages(self):
        return self.ages

    def get_info(self):
        return f"My name is '{self.get_name()}', my ages is {self.get_ages()}"

    def get_children(self):
        return copy.deepcopy(self.children)

    def add_children(self, child):
        if not child in self.children and self.ages - child.ages >= 16:
            self.children.append(child)

    def do_calm(self, child: Children):
        if child in self.children:
            child.calm(False)
            print("Child is not calm")

    def do_feed(self, child: Children):
        if child in self.children:
            child.hungry(False)
            print("Child is not hungry!")

    def __str__(self):
        return f"Parent: [name = {self.name}, ages = {self.ages}, children = {[s.__str__() for s in self.children]}]"


p = Parent("Ivan", 45)
c1 = Children("Sveta", 12)
c2 = Children("Sergey", 8)
print(p, c1, c2, sep='\n')

p.add_children(c1)
p.add_children(c2)
print(p)

p.do_calm(c1)
p.do_feed(c2)
print(p)

# Parent: [name = Ivan, ages = 45, children = []]
# Children: name = Sveta, ages = 12, calm = True, hungry = True
# Children: name = Sergey, ages = 8, calm = True, hungry = True
# Parent: [name = Ivan, ages = 45, children = ['Children: name = Sveta, ages = 12, calm = True, hungry = True', 'Children: name = Sergey, ages = 8, calm = True, hungry = True']]
# Child is not calm
# Child is not hungry!
# Parent: [name = Ivan, ages = 45, children = ['Children: name = Sveta, ages = 12, calm = False, hungry = True', 'Children: name = Sergey, ages = 8, calm = True, hungry = False']]
