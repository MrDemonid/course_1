""" 
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:                                       Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам      Парам пам-пам
"""
# org = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# # org = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'

# evens = 'ауоыиэяюёе'

# def check(s):
#     words = s.split()
#     orglen = -1
#     if len(words) <= 1:
#         return -1
#     for i in words:
#         lst = list(filter(lambda n: n in evens, i))
#         if orglen == -1:
#             orglen = len(lst)
#         else:
#             if orglen != len(lst):
#                 return 0
#     return 1

# res = check(org)
# if res == 1:
#     print('Парам пам-пам')
# elif res == 0:
#     print('Пам парам')
# else:
#     print('Количество фраз должно быть больше одной!')

# ------------------------------------------------
    
# vowels = ['а','у','о','ы','и','э','я','ю','ё','е']
# stroka = org.split()
# count_vowels = []
# for i in stroka:
#     count = len([x for x in i if x.lower() in vowels])
#     count_vowels.append(count)

# if count_vowels.count(count_vowels[0]) == len(count_vowels):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')






""" 
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.
Ввод:                                           Вывод:
print_operation_table(lambda x, y: x * y)       1 2 3 4 5 6
                                                2 4 6 8 10 12
                                                3 6 9 12 15 18
                                                4 8 12 16 20 24
                                                5 10 15 20 25 30
                                                6 12 18 24 30 36 
rows - строки
columns - столбцы
 """
def print_operation_table(op, num_rows=9, num_columns=9):
    if num_rows < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    for x in range(1, num_columns+1):
        for y in range(1, num_rows+1):
            n = op(x, y)
            if (y < num_rows):
                print(n, end = ' ')
            else:
                print(n)


print_operation_table(lambda x, y: x / y, 4, 4)
# 1.0 0.5 0.3333333333333333 0.25
# 2.0 1.0 0.6666666666666666 0.5
# 3.0 1.5 1.0 0.75
# 4.0 2.0 1.3333333333333333 1.0

# -------------------------------------------
def print_operation_table(operation, num_rows=6, num_columns=6):
    if num_rows < 2 or num_columns < 2:
        print('error')
    else:
        print(' '.join(list(map(str, range(1, num_columns + 1)))))
        for i in range(2, num_rows + 1):
            print(i, end = ' ')
            for j in range(2, num_columns + 1):
                print(operation(i, j), end=' ')
            print()

print_operation_table(lambda x, y: x / y, 4, 4) 

# -----------------------------
# org = ["udp", "next", "rest"]
# s = " ".join(org)
# print(s)

""" 
print_operation_table(lambda x, y: x * y, 3, 3)
print_operation_table(lambda x, y: x + y, 4, 4)
print_operation_table(lambda x, y: x * y, 1, 2)
print_operation_table(lambda x, y: x - y, 5, 5)
print_operation_table(lambda x, y: x / y, 4, 4)

"""