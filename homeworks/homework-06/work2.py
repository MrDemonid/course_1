"""
Задача 2. Модуль для удаления дублирующихся подряд символов.

Напишите модуль с функцией, которая принимает строку и возвращает строку с
удаленными дублирующимися подряд идущими символами. Например, строка
"aabbccaa" должна быть преобразована в "abca".
"""


def exclude_double(source: str) -> str:
    res = source[0]
    for i in range(1, len(source)):
        if source[i-1] != source[i]:
            res += source[i]
    return res


if __name__ == '__main__':
    print(exclude_double("aabbccaakllllm"))


