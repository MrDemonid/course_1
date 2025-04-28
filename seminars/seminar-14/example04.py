"""
Задание №4.

Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
    возврат строки без изменений
    возврат строки с преобразованием регистра без потери символов
    возврат строки с удалением знаков пунктуации
    возврат строки с удалением букв других алфавитов
    возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

import pytest
from example01 import replacement

def test_1():
    assert replacement('test string') == 'test string', 'Ошибка 1'

def test_2():
    assert replacement('Test String') == 'test string', "Ошибка 2"

def test_3():
    assert replacement('>Test string.') == 'test string', "Ошибка 3"

def test_4():
    assert replacement('Test string - это строка для теста.') == 'test string     '

def test_5():
    assert replacement('Test string, это строка,this REAL string!') == 'test string  this real string'


if __name__ == '__main__':
    pytest.main(['-v'])





