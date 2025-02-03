"""
Задание №2.
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный

Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

def get_hash(obj):
    try:
        return hash(obj)
    except TypeError:
        return -1


def get_hash2(obj):
    if callable(getattr(obj, "__hash__", None)):
        return hash(obj)
    return -1



data = [1, 1.2, 0b11110000, 'Строка', (1, 2), {1:"Red", 2:"Blue"}, None, True]

for i, value in enumerate(data, start=1):
    print(f"[{i}] {value}, type = {type(value)}, address = {id(value)}, size: {value.__sizeof__()}, hash code: {get_hash(value)}")
    if isinstance(value, int):
        print("\tthe value is integer")
    if isinstance(value, str):
        print("\tthe value is string")

