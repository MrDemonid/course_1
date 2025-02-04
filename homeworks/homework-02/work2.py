"""
Задание 2. Преобразование числа в шестнадцатеричное представление.

    Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата.
"""

'''
    Аналог hex(). Для ускорения используются битовые операции, 
    а вместо конкатенации строк добавление в конец массива,
    с последующем преобразованием его в строку. 
'''
def my_hex(n: int) -> str:
    _hex = "0123456789ABCDEF"
    res = []
    if n < 0:
        n = -n
        res.append("-")
    while True:
        res.append(_hex[n & 0b00001111])
        n >>= 4
        if n == 0:
            break
    return "".join(reversed(res))



num = int(input("Введите целое число: "))
print(f"my func : 0x{my_hex(num)}\noriginal: {hex(num)}")
