"""
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""

import string
from random import randint, choice, sample

def _check_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for ch in vowels:
        if ch in s:
            return True
    return False


def gen_names(file_name, num_names):
    alph= [ch for ch in string.ascii_lowercase]
    with open(file_name, 'w', encoding='utf-8') as f:
        while num_names:
            length = randint(4, 7)
            while True:
                name = "".join(sample(alph, length)).capitalize()
                if _check_vowels(name):
                    break
            f.write(f"{name}\n")
            num_names -= 1


if __name__ == '__main__':
    gen_names('./datas/names.txt', 30)
