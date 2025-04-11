"""
Задача 3. Класс с динамическим созданием экземпляров.

Создайте класс Book, который создает экземпляры с помощью __new__.
Убедитесь, что каждый экземпляр имеет уникальный идентификатор.
"""

class Book:

    _id = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._id = cls._id
        cls._id += 1
        return instance

    def __init__(self, author, title, date):
        self.author = author
        self.title = title
        self.date = date

    def __str__(self):
        return f"Книга[{self._id}]: {self.author}. '{self.title}'. {self.date} г."

if __name__ == '__main__':
    b = Book('Майн Рид', "Вождь краснокожих", 1959)
    print(b)
    t = Book("Фенимор Купер", "Последний из Могикан", 1964)
    print(t)
