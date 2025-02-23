"""
Задание №1
✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""


s = input('Enter four numbers, with "/" separator: ').split('/')
if len(s) < 4:
    print("Error: numbers must be four or greater!")
    quit()

a, b, c, *d = s.copy()
res = {b:int(a), c: tuple([int(n) for n in d])}
print(res)


