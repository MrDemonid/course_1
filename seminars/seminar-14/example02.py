"""
Задание №2.

Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
    возврат строки без изменений
    возврат строки с преобразованием регистра без потери символов
    возврат строки с удалением знаков пунктуации
    возврат строки с удалением букв других алфавитов
    возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

def replacement(src: str) -> str:
    """ Удаляет из строки все символы кроме латинского алфавита и пробелов
    >>> replacement('test string')
    'test string'
    >>> replacement('Test String')
    'test string'
    >>> replacement('>Test string.')
    'test string'
    >>> replacement('Test string - это строка для теста.')
    'test string     '
    >>> replacement('Test string, это строка,this REAL string!')
    'test string  this real string'
    """
    res = ""
    for ch in src.lower():
        if 'a' <= ch <= 'z' or ch == ' ':
            res += ch
    return res
