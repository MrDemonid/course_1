"""
Задание №1.

Создайте функцию-замыкание, которая запрашивает два целых числа:
    - от 1 до 100 для загадывания;
    - от 1 до 10 для количества попыток;
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""

def main_decorator():
    number = int(input("Enter number from range 1-100: "))
    count = int(input("Enter changes from range 1-10: "))
    def bulls_and_cows():
        n = -number
        for _ in range(count):
            n = int(input("-- my number (1-100)?: "))
            if n == number:
                print("You win!")
                return
            if n > number:
                print("  -- my number is less!")
            else:
                print("  -- my number is great!")
        print(f"You loss! number is {number}")
    return bulls_and_cows


f = main_decorator()
f()
