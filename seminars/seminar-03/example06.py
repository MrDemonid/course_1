"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

inp = "Строки нумеруются начиная с единицы"

mas = inp.split()
max_len = len(max(mas, key=len))  # без key не будет работать, поскольку ищет наибольшее слово, а не по длине!

for index, elem in enumerate(sorted(mas), 1):
    print(f"{index}: {elem:>{max_len}}")

print(mas)
