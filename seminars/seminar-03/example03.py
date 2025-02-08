"""
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
    ключ — тип элемента,
    значение — список элементов данного типа.
"""

inp = (1, 2.1, True, None, 'text', 3, 4, 5, False, 'elem')

# Вариант 1
res = {}

for elem in inp:
    t = type(elem)
    val = [elem]
    if t in res:
        res[t].append(elem)
    else:
        res[t] = val

print(res)


# Вариант 2
res = {}

for elem in inp:
    res.setdefault(type(elem), []).append(elem)

print(res)
