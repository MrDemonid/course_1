############### Списки

# lst = []
# lst = list()
# lst = [2, 3.1, "Family"]

# print(type(lst[0]))
# print(type(lst[1]))
# print(type(lst[2]))
# print(lst)              # [2, 3.1, 'Family']
# print(*lst)             # 2 3.1 Family

# lst = [2, 3.1, "Family"]
# for i in lst:
#     print(i)

# print(len(lst))


# lst = [2, 3.1, "Family"]
# print(lst[0])
# print(lst[-1])
# print(lst[-3])


# lst = [2, 3.1, "Family"]
# print(lst)
# lst.append(9)
# print(lst)
# mas = []
# for i in range(4):
#     mas.append(i)
#     print(mas)


# удаление последнего элемента списка
# lst = [12, 7, 9, 5]
# print(lst)              # [12, 7, 9, 5]
# print(lst.pop())        # 5
# print(lst)              # [12, 7, 9]
# print(lst.pop())        # 9
# print(lst)              # [12, 7]

# удаление конкретного элемента из списка
# lst = [12, 7, "Name", 5]
# print(lst.pop(0))
# print(lst)
# print(lst.pop(1))
# print(lst)

# добавление элемента на нужную позицию
# lst = [7, 5]
# print(lst)
# lst.insert(0, 12)
# print(lst)
# lst.insert(2, 'Name')
# print(lst)

# срезы списков
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst[0])
# print(lst[1])
# print(lst[len(lst)-1])
# print(lst[-1])
# print(lst[-5])
# print(lst[:])
# print(lst[:3])
# print(lst[5:])
# print(lst[len(lst)-2:])
# print(lst[2:9])
# print(lst[6:-18])
# print(lst[0:len(lst):6])
# print(lst[::6])


############### кортежи (это список с защитой элементов от изменений)
# t = ()
# print(type(t))
# t = (1)             # это уже не кортеж
# print(type(t))
# t = (1,)            # запятая в конце - кортеж
# print(type(t))

# v = [1,2,5]
# print(v)
# print(type(v))
# v = tuple(v)
# print(v)
# print(type(v))
# # v[1] = 6              # вызовет ошибку
# # разобьём кортеж на переменные
# a, b, c = v
# print(a, b, c)

# t = (1,4,9,)
# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(t[i])


############### Словари
# v = {}
# v = {'left': '<-', "right": '->'}
# print(type(v))
# print(v)
# print(v['left'])

# v = dict()
# v = {'left': '<-', 'right': '->', 12: 'Word'}
# for i in v:
#     print(i)
# print('cycle with format:')
# for i in v:
#     print('{}: {}'.format(i, v[i]))
# print('three cycle')
# for (a,b) in v.items():
#     print(a,b)

# print(v.items())


############### Множества
# col = {'red', 'green', 'blue'}
# print(col)
# col.remove('green')
# print(col)
# col.discard('green')
# print(col)
# col.clear()
# print(col)

# операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            # копирование множества
# print(c)
# u = a.union(b)          # объединение множеств
# print(u)
# i = a.intersection(b)   # пересечение множеств
# print(i)

# q = a.union(b).difference(a.intersection(b))
# print(q)

# d = frozenset(a)        # замороженное множество (неизменное)
# print(d)


############### List Comprehension (Генератор списков)
list_1 = [i for i in range(1,5)]    # [1,2,3,4]
print(list_1)

list_1 = [i for i in range(1,11) if i % 2 == 0]    # [1,2,3,4]
print(list_1)

list_1 = [(i,i) for i in range(1,11) if i % 2 == 0]    # [1,2,3,4]
print(list_1)


list_1 = [i*2 for i in range(10) if i % 2 == 0]    # [1,2,3,4]
print(list_1)
