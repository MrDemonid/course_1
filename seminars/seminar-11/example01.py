"""
Задание №1.

Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
"""
import time


class MyStr(str):
    def __new__(cls, author, val):
        c = super().__new__(cls, val)         # создаем класс str
        c.author = author
        c.time = time.time()
        return c

    def __str__(self):
        return f"Author: '{self.author}', created at {self.time}: '{super().__str__()}'"

    def __repr__(self):
        return f"MyStr({self.author}, {super().__str__()}"


s = MyStr("Andrey", "This is test string.")
t = MyStr("Ivan", "This not test")
print(s)

datas = [MyStr("Andrey", "string 1"), MyStr("Ivan", "string 2")]
print(datas)

res = s.split(" ")
print(res)
