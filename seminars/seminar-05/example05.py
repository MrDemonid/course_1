"""
Задание №5
✔ Напишите программу, которая выводит на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
"""

# Вариант 1
def conv():
    for n in range(1, 101):
        res = n
        if n % 3 == 0 and n % 5 == 0:
            res = 'FizzBuzz'
        elif n % 3 == 0:
            res = 'Fizz'
        elif n % 5 == 0:
            res = 'Buzz'
        yield res


gen = conv()
for i in gen:
    print(i, end=', ')
print('\x08\x08')


# Вариант 2
gen = ('FizzBuzz' if n % 3 == 0 and n % 5 == 0 else ('Fizz' if n % 3 == 0 else ('Buzz' if n % 5 == 0 else n)) for n in range(1, 101))
for i in gen:
    print(i, end=', ')
print('\x08\x08')


