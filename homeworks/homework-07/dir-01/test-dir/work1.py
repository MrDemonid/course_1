"""
Задание 1. Удаление дубликатов из списка.
    Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.
"""

inp = [1, 2, 3, 4, 5, 1, 3, 6, 7, 3, 7]

# Вариант 1
res = []
for elem in inp:
    if inp.count(elem) > 1 and not elem in res:
        res.append(elem)

print(res)

# Вариант 2
res = list({elem for elem in inp if inp.count(elem) > 1})
print(res)
