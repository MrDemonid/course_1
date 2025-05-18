""" 
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
# # первое решение
# array = [1, 1, 2, 0, -1, 3, 4, 4]

# m = set(array)
# print(len(m))


# # второе решение
# def is_present(mas, item):
#     for i in mas:
#         #print('> ',i, item)
#         if i == item:
#             return True
#     return False

# print('Enter array, or "q" for end')
# mas = []
# while True:
#     n = input()
#     if n == 'q' or n == 'Q':
#         break
#     if not is_present(mas, int(n)):
#         mas.append(int(n))
# print(mas)
# print('num elements: ', len(mas))


""" 
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""
# # сдвиг массива вправо
# def rar(mas, cnt):
#     while cnt > 0:
#         l = mas[-1]
#         for i in range(len(mas)-1, 0, -1):
#             mas[i] = mas[i-1]
#         mas[0] = l
#         cnt -= 1

# # сдвиг массива влево
# def ral(mas, cnt):
#     while cnt > 0:
#         f = mas[0]
#         for i in range(1, len(mas)):
#             mas[i-1] = mas[i]
#         mas[-1] = f
#         cnt -= 1

# print('Enter array, or "q" for end')
# mas = []
# while True:
#     n = input()
#     if n == 'q' or n == 'Q':
#         break
#     mas.append(int(n))

# print(mas)
# if len(mas) > 0:
#     n = int(input('Enter k: '))
#     rar(mas, n)

# print(mas)



""" 
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
"""
# 1-й вариант со множеством
# dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# out = set()

# for i in dic:
#     for j in i:
#         out.add(i[j].strip())   # добавляем, обрезая пробелы
# print(out)

# # 2-й вариант с функцией поиска

# sout = []

# def is_present(mas, string):
#     for i in mas:
#         if i == string:
#             return True
#     return False

# for i in dic:
#     for j in i:
#         s = i[j].strip()    # s - эл. с обрезанными пробелами
#         if not is_present(sout, s):
#             sout.append(s)
# print(sout)





""" 
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""
# def inp_array(m):
#     print('Enter array numbers, or "q" for exit')
#     while True:
#         s = input()
#         if s == 'q' or s == 'Q':
#             break
#         m.append(int(s))

# def get_greats(mas):
#     n = 0
#     for i in range(1, len(mas)):
#         if mas[i] > mas[i-1]:
#             n += 1
#     return n
# mas = []
# inp_array(mas)
# print(mas)
# print('Result: ', get_greats(mas))

k = 'ноутбук'   # 12

alf = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10,
        'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2, 'Б':3, 
        'Г':3, 'Ё':3, 'Ь':3, 'Я':3, 'Й':4, 'Ы':4, 'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8, 'Ф':10, 'Щ':10, 'Ъ':10
}

sum = 0
for i in k:
    ch = i.upper()
    sum += alf[ch]
print(sum)    



""" 
eng = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
rus = [1,3,1,3,2,1,3,5,5,1,4,2,2,2,1,1,2,1,1,1,2,10,5,5,5,8,10,10,4,3,8,8,3]

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
 """