""" 
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""
# n = int(input("Введите число: "))

# ff = 1
# while n > 0:
#     ff = ff * n
#     n = n - 1

# print("Факториал = ", ff)


""" 
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""
# a = int(input("Введите число: "))
# fn1 = 1
# fn = 0
# res = 0
# while True:
#     if fn > a:
#         res = -1
#         break
#     if fn == a:
#         break
#     fn2 = fn1
#     fn1 = fn
#     fn = fn1 + fn2      # f(n) = f(n-1)+f(n-2)
#     print(fn)
#     res = res + 1

# print("Число: ", res)


# n = int(input('Введите число: '))
# max_day = 0
# t = 0
# for i in range(n):
#     x = int(input('Введите число: '))
#     if (x <= 0):
#         if max_day < t:
#             max_day = t
#         t = 0
#     else:
#         t += 1

# if max_day < t:
#     max_day = t
# print(max_day)


