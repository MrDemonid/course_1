"""
Задание №6
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт» без перехода на новую строку.
"""

gen = ("\n" if i == 10 else f"{i} X {j:>2} = {(i * j):>2}    " for j in range(2, 11) for i in range(2, 11))

print('', *gen)
