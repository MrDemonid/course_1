"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
"""
import copy
from random import randint
from timeit import timeit

l = [randint(0, 50000) for _ in range(20000)]


def buble_sort(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def selected_sort(lst):
    for i in range(0, len(lst) - 1):
        _min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[_min]:
                _min = j
        if min != i:
            lst[i], lst[_min] = lst[_min], lst[i]
    return lst


# print(buble_sort(l))
# print(selected_sort(l))


# замер скорости
print("do test buble...")
print(timeit('buble_sort(copy.deepcopy(l))', globals=globals(), number=3))  # 72.43351979996078
print("do test selected...")
print(timeit('selected_sort(copy.deepcopy(l))', globals=globals(), number=3))  # 27.931663200026378

# Xeon E3-1270 v3:
# buble    - 72.43351979996078
# selected - 27.931663200026378

# Xeon E5-1650 v4
# buble    - 41.650159599999824
# selected - 19.807272600000033


