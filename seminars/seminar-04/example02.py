"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию
"""

def str_to_chr(s: str) -> list:
    return sorted({ord(ch) for ch in s}, reverse=True)

print(str_to_chr("Hello world!"))
