"""
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""


# Решение 1
def sum_digits(n):
    res = 0
    while n > 0:
        res = res + n % 10
        n = n // 10
    return res

gen = (n for n in range(0, 100, 2) if sum_digits(n) != 8)
for n in gen:
    print(n, end=', ')
print('\x08\x08')

# Решение 2
gen = (n for n in range(0, 100, 2) if sum(list(map(int, str(n)))) != 8)
for n in gen:
    print(n, end=', ')
print('\x08\x08')

# Решение 3
gen = (n for n in range(0, 100, 2) if sum([int(ch) for ch in str(n)]) != 8)
for n in gen:
    print(n, end=', ')
print('\x08\x08')

# gen = (n for n in range(0, 100, 2) if sum(list(map(int, str(n)))) != 8)
# print(*gen)
