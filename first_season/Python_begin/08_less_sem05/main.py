""" 
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1)+fib(n-2)

# n = int(input('Enter number: '))
# print(f"[{n}] = {fib(n)}")
# # for i in range(1, 13):
# #     print(fib(i),end=' ')
# # print()


""" 
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""
# def CorrectGrade(lst):
#     for i in range(len(lst)):
#         n = lst.pop(i)
#         if n > 3:
#             n = 1
#         lst.insert(i, n)

# grades = []

# n = int(input('Enter len: '))
# while (n > 0):
#     grades.append(int(input('Enter points: ')))
#     n -= 1
# print(grades)
# CorrectGrade(grades)
# print(grades)

## lesson:
# list1 = [1, 3, 3, 3, 4]
# maxx = max(list1)
# minn = min(list1)

# # for i in range(len(list1)):
# #     if list1[i] == maxx:
# #         list1[i] == min
# list1 = [minn if i == maxx else i for i in list1]
# print(list1)



""" 
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
"""
# def isPrime(n):
#     if (n < 0):
#         n = -n
#     sq = int(n**(0.5))  # простой множитель не может быть больше корня квадратного числа 
#     print(f'sqrt({n}) = {sq}')
#     for i in range(2, sq+1):
#         if n % i == 0:
#             return False
#     return True
# n = int(input('Enter num: '))
# if is_prime(n):
#     print('yes')
# else:
#     print('no')



""" 
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. 
В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
 """
# def printReverse(cnt):
#     if cnt <= 0:
#         return
#     n = int(input('Enter elem: '))    
#     printReverse(cnt-1)
#     print(n, end= ' ')

# cnt = int(input('Enter len: '))    
# printReverse(cnt)

# # через строку
# def print_rev(cnt):
#     if cnt <= 0:
#         return ''
#     n = int(input('Enter elem: '))
#     return print_rev(cnt-1) + f"{n} "

# cnt = int(input('Enter len: '))    
# print(print_rev(cnt))



""" 
Домашка
"""
""" 
Напишите функцию f, которая на вход принимает два числа a и b, 
и возводит число a в целую степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.
Пример:
a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8 
"""
# def f(a, b):
#     if b > 1:
#         a = a * f(a, b-1)
#     return a

# print(f(2, 3))



""" 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
Функция не должна ничего выводить, только возвращать значение.
Пример:
sum(2, 2)
# 4
"""
# def sum(a, b):
#     if b <= 0:
#         return a
#     a = sum(a,b-1) + 1
#     return a
# print(sum(1,6))

