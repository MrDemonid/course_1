"""
Задание №3.

Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
    возврат строки без изменений
    возврат строки с преобразованием регистра без потери символов
    возврат строки с удалением знаков пунктуации
    возврат строки с удалением букв других алфавитов
    возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import unittest

from example01 import replacement

class TestReplacement(unittest.TestCase):

    def test_1(self):
        self.assertEqual(replacement('test string'), 'test string')

    def test_2(self):
        self.assertEqual(replacement('Test String'), 'test string')

    def test_3(self):
        self.assertEqual(replacement('>Test string.'), 'test string')

    def test_4(self):
        self.assertEqual(replacement('Test string - это строка для теста.'), 'test string     ')

    def test_5(self):
        self.assertEqual(replacement('Test string, это строка,this REAL string!'), 'test string  this real string')


if __name__ == '__main__':
    unittest.main()
