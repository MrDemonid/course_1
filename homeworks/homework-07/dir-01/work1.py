"""
Задание 1. Модуль для подсчета количества повторений слов.

Создайте модуль с функцией, которая получает список слов и возвращает
словарь, в котором ключи — это слова, а значения — количество их повторений
в списке.
"""

def get_word_count(source: list[str]):
    d = dict()
    for word in source:
        d.setdefault(word, 0)
        d[word] += 1
    return d



if __name__ == '__main__':
    print(get_word_count(['assa', 'massa', 'assa', 'kassa', 'assa', 'kassa']))

