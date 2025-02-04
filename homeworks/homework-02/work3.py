"""
Задача 3. Перевод целого числа в римское число.

    Программа принимает целое число и возвращает его римское представление в
виде строки.
"""

numbers = [1000,    900,    500,    400,    100,    90,     50,     40,     10,     9,      5,      4,      1]
symbols = ['M',     'CM',   'D',    'CD',   'C',    'XC',   'L',    'XL',   'X',    'IX',   'V', '  IV',    'I']

def to_rome(year):
    res = []
    for i in range(len(numbers)):
        k = numbers[i]
        while year - k >= 0:
            year -= k
            res.append(symbols[i])
    return "".join(res)


y = int(input("Введите год, от 1 до 3999: "))
if 0 < y <= 3999:
    rome = to_rome(y)
    print(f"year {y} is to rome at: {rome}")

