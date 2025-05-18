# # Ссылки на функции

# def calck1(a, b):
#     return a + b

# def calck2(a, b):
#     return a * b

# def do_calck(op, a, b):
#     return op(a, b)

# t = calck1
# n = do_calck(calck1, 5, 45)
# m = do_calck(calck2, 5, 45)
# k = t(10,15)
# print(n)
# print(m)
# print(k)

# #########################################################

# # Лямбда-функции

# calck1 = lambda a,b: a + b
# print(calck1(5,2))

# # выбираем из списка только чётные элементы
# lst = [1,3,4,6,10,11,15,14,7,12]
# res = list(filter(lambda x: (x % 2 == 0), lst))
# print(res)  

# # условия в лямбдах
# maxx = lambda a, b: a if a > b else b
# print(maxx(5, 3))

""" 
В списке хранятся числа. Нужно выбрать только чётные числа и составить
список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
"""
# org = [1, 2, 3, 5, 8, 15, 23, 38]

# def where(op, lst):
#     return [(i, i*i) for i in lst if op(i)]

# res = where(lambda n: (n % 2 == 0), org)
# print(res)



#########################################################

# MAP()

# lst = [i for i in range(1, 10)]
# lst = list(map(lambda x: x+10, lst))
# print(lst)

""" 
C клавиатуры вводится некий набор чисел, в качестве разделителя
используется пробел. Этот набор чисел будет считан в качестве строки. Как
превратить list строк в list чисел?
"""
# lst = list(map(int, input().split()))
# print(lst)



#########################################################

# FILTER()

# lst = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 5 == 0, lst))
# print(res)                                      # [15, 65, 175]



#########################################################

# ZIP()

# users = ['Anna', 'Grisha', 'Ben', 'Andrey', 'Anton', 'Sergey']
# ages = [18, 23, 63, 20, 47, 18, 32]
# present = [1200, 1100, 500, 5200]

# res = list(zip(users, ages, present))
# print(res)



#########################################################

# ENUMERATE()

# lst = ['Казань', 'Смоленск', 'Рязань']
# res = list(enumerate(lst))
# print(res)
