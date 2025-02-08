"""
Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

inp = [1, 2, 3, 2, 4, 5, 3, 6, 6, 3]

# Вариант 1
res = [item for item in inp if inp.count(item) != 2]

print(res)


# Вариант 2

res = []
for item in inp:
    if inp.count(item) != 2:
        res.append(item)

print(res)
