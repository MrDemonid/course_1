"""
Задание №1.

Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""

def replacement(src: str) -> str:
    res = ""
    for ch in src.lower():
        if 'a' <= ch <= 'z' or ch == ' ':
            res += ch
    return res


if __name__ == '__main__':
    d = replacement("Test 123string. for #semi!nar 14 Ура")
    print(d)
