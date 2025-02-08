"""
Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
✔ Нумерация начинается с единицы
"""

inp = [1, 2, 3, 2, 4, 5, 3, 6, 3]

# Вариант 1
res = []

for i in range(len(inp)):
    if inp[i] & 1 != 0:
        res.append(i + 1)

print(res)

# Вариант 2
res = [(index + 1) for index in range(len(inp)) if inp[index] & 1 != 0]

print(res)

# Вариант 3
res = [(index + 1) for index, elem in enumerate(inp) if elem & 1 != 0]
print(res)
