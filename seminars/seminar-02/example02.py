"""
Задание №3
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
"""

def my_bin(n: int) -> str:
    _bin = "01"
    res = []
    while True:
        res.append(_bin[n & 1])
        n >>= 1
        if n == 0:
            break
    return "".join(reversed(res))


def my_oct(n: int) -> str:
    _oct = "01234567"
    res = []
    while True:
        res.append(_oct[n & 0b00000111])
        n >>= 3
        if n == 0:
            break
    return "".join(reversed(res))

def my_hex(n: int) -> str:
    _hex = "0123456789ABCDEF"
    res = []
    while True:
        res.append(_hex[n & 0b00001111])
        n >>= 4
        if n == 0:
            break
    return "".join(reversed(res))


num = int(input("Введите целое число: "))
if isinstance(num, int):
    print(f"input: '{num}'.")
    print(f"  bin: {my_bin(num)}, control is: {bin(num)}")
    print(f"  oct: {my_oct(num)}, control is: {oct(num)}")
    print(f"  hex: {my_hex(num)}, control is: {hex(num)}")

