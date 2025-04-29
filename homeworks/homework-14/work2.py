"""
Задача 2. Тестирование класса с использованием unittest.

Напишите класс Library, который управляет книгами. Класс должен поддерживать следующие методы:
    ● add_book(title): добавляет книгу в библиотеку.
    ● remove_book(title): удаляет книгу из библиотеки.
    ● list_books(): возвращает список всех книг в библиотеке.

При попытке удалить книгу, которая не существует, должно выбрасываться исключение BookNotFoundError.
Для тестирования используйте unitest.
"""


class BookNotFoundError(Exception):
    def __init__(self):
        super().__init__("Книга не найдена!")


class Library:
    def __init__(self, titles: list):
        self._titles = list()
        for title in titles:
            self._titles.append(title)

    def add_book(self, title):
        if isinstance(title, str):
            if title is None or len(title.strip()) == 0:
                raise ValueError("Название не может быть пустой строкой!")
            if title in self._titles:
                raise ValueError("Книга уже присутствует в библиотеке!")
            self._titles.append(title)
        else:
            raise TypeError("Название должно быть строкой!")

    def remove_book(self, title):
        if isinstance(title, str):
            if not title in self._titles:
                raise BookNotFoundError()
            self._titles.remove(title)
        else:
            raise TypeError("Название должно быть строкой!")

    def list_books(self):
        res = list()
        for t in self._titles:
            res.append(t)
        return res


import unittest

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library(['Туманность Андромеды', 'Маленькие дикари'])

    def test_init(self):
        self.assertEqual(self.lib.list_books(), ['Туманность Андромеды', 'Маленькие дикари'])

    def test_add_normal(self):
        self.lib.add_book('Посёлок')
        self.assertIn('Посёлок', self.lib.list_books())

    def test_add_value(self):
        self.assertRaises(ValueError, self.lib.add_book, '')

    def test_add_type(self):
        self.assertRaises(TypeError, self.lib.add_book, 1974)

    def test_remove_normal(self):
        self.lib.remove_book('Туманность Андромеды')
        self.assertNotIn('Туманность Андромеды', self.lib.list_books())

    def test_remove_except(self):
        self.assertRaises(BookNotFoundError, self.lib.remove_book, 'Посёлок')

    def test_remove_type(self):
        self.assertRaises(TypeError, self.lib.remove_book, 1974)


if __name__ == '__main__':
    unittest.main()
