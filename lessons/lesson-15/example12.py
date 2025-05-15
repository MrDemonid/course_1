# Замена значений полей namedtuple

from collections import namedtuple


Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(b)


# Сортировка
data = [Point(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11), Point(2, 202, 1)]
print(sorted(data))


# Изменение типа свойства - объект перестает быть хэшируемым и уже не подходит для ключей словаря!
t = Point(1, [2, 3, 4], 5)
print(t)

s = {a : "first", b : "two"}
print(s)
s.update({t : "bad point"})     # TypeError: unhashable type: 'list'

