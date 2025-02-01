"""
Задача 3. Простые числа.
Напишите программу, которая считает количество простых чисел в заданной
последовательности и выводит ответ на экран.
Простое число делится только на себя и на единицу. Последовательность
задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна
итерация — одно число.
"""
from math import sqrt

"""
    Ввод размеров сторон треугольника. 
"""
def input_number(message: str):
    while True:
        try:
            num = int(input(f"{message}: "))
            if num < 0:
                quit()
            return num
        except KeyboardInterrupt:
            print("Ошибка ввода, попробуйте снова.")
            continue
        except ValueError:
            print("Неверные данные, попробуйте снова.")
            continue
        except EOFError:
            print("Неожиданный конец ввода, попробуйте снова.")
            continue


"""
    Оптимизированный алгоритм определения простого числа, учитывающее некоторые факторы:
        1) Если у числа есть делитель больше sqrt(n), то обязательно
            есть делить и меньше sqrt(n).
        2) Есть только одно простое число делящееся на 2 - это сама двойка, все остальные - составные.
            Поэтому сразу проверяем делимость на 2.
        3) Вытекает из п.2 - можно сразу отбросить проверку на четные числа, поскольку мы уже сделали
            проверку делимости на 2.
        4) Число 3 - это наименьшее нечетное простое число. И чтобы упростить алгоритм, мы его 
            проверяем сразу же.
"""
def is_prime(number):
    if number < 2 or (number % 2) == 0:
        return False
    if number == 2 or number == 3:
        return True

    n = sqrt(number)
    for divider in range(3, int(n), 2):
        if number % divider == 0:
            return False
    return True


