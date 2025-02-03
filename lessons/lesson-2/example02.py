"""
Получаем зависимость размера объекта типа int,
от размера хранимого в нём значения.
"""
import sys

STEP = 65536
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP
