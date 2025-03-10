"""
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""

import string
from random import randint, choice, sample


def _check_vowels(s):
    """ Проверяет, есть ли в слове хотя бы одна согласная буква """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return any(l in vowels for l in s)


def gen_names(file_name, num_names):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_names):
            length = randint(4, 7)
            while True:
                name = "".join(sample(string.ascii_lowercase, length)).title()
                if _check_vowels(name):
                    break
            f.write(f"{name}\n")


if __name__ == '__main__':
    gen_names('./datas/names.txt', 30)
