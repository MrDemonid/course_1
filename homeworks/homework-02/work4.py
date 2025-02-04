"""
Задача 4. Сумма и произведение дробей.

    Программа принимает две строки вида "a/b" - дробь с числителем и
знаменателем. Возвращает сумму и произведение дробей. Для проверки
используется модуль fractions.
"""

from fractions import Fraction

'''
    Наибольший общий делитель.
'''
def NOD(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    return a + b


'''
Сложение дробей.
    n1, d1 - первая дробь (числитель и знаменатель)
    n2, d2 - вторая дробь (числитель и знаменатель)
'''
def frac_add(n1, d1, n2, d2):
    # самый простой способ привести дроби к общему знаменателю - это перемножить на их знаменатели
    tn1 = n1 * d2
    res_d = d1 * d2
    tn2 = n2 * d1
    res_n = tn1 + tn2
    # сокращаем дробь
    nod = NOD(res_n, res_d)
    return (res_n // nod), (res_d // nod)


'''
Перемножение дробей.
    n1, d1 - первая дробь (числитель и знаменатель)
    n2, d2 - вторая дробь (числитель и знаменатель)
'''
def frac_mul(n1, d1, n2, d2):
    res_n = n1 * n2
    res_d = d1 * d2
    # сокращаем дробь
    nod = NOD(res_n, res_d)
    return (res_n // nod), (res_d // nod)


'''
    Основная программа.
'''
frac1 = input("Введите первую дробь (в формате a/b): ")
frac2 = input("Введите вторую дробь (в формате a/b): ")

numerator1, denominator1 = map(int, frac1.split('/'))
numerator2, denominator2 = map(int, frac2.split('/'))

'''
    Решаем с помощью наших функций.
'''
resn, resd = frac_add(numerator1, denominator1, numerator2, denominator2)
print(f"Сумма дробей: {resn}/{resd}")
resn, resd = frac_mul(numerator1, denominator1, numerator2, denominator2)
print(f"Произведение дробей: {resn}/{resd}")

'''
    Проверяем с помощью модуля fraction.
'''
f1 = Fraction(frac1)
f2 = Fraction(frac2)

print(f"Сумма дробей: {f1 + f2}")
print(f"Произведение дробей: {f1 * f2}")
