# def summ(n, s='Summ is '):
#     print(s,end='')
#     res = 0
#     for i in range(1, n+1):
#         res += i
#     return res

# print(summ(5))
# print(summ(5, 'Result = '))


# def summ(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(summ('b','a','d'))
# print(summ('a','b','c','d'))

# def summ(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res

# print(summ(1,2,3,4,5))
# print(summ(10,20))

"""
Экспорт функций из других модулей
"""
# import module1
# print(module1.max1(5,9))
# print(module1.max1(4,-10))

# import module1 as m1
# print(m1.max1(5,9))
# print(m1.max1(4,-10))

# from module1 import max1
# print(max1(12,9))

# from module1 import *
# print(max1(-4,10))
# print(min1(-4,10))

'''
Рекурсия
'''
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# for i in range(3,7):
#     print(f"[{i}]: {fib(i)}")


'''
Алгоритмы
'''
# from csorts import qsort
# mas = [12,5,2,23,84,-1,34,23,90,1]
# print(mas)
# out = qsort(mas)
# print(out)

from csorts import *

mas = [12,5,2,21,84,-1,34,23,90,1]
print(mas)
merge_sort(mas)
print(mas)



