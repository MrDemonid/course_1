"""
Задача 4. Генератор подстрок.

Напишите генераторную функцию substrings(s), которая принимает строку
s и возвращает генератор всех возможных подстрок этой строки.
На вход подается строка abc
На выходе будут выведены обозначения:
a
ab
abc
b
bc
c
"""


def substrings(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            yield s[i: (j + 1)]


for k in substrings('abcd'):
    print(k)

