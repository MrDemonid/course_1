a, b, c = 'ABC'
print(a, b, c)

a, b, c = ('one', 'two', 'three')
print(a, b, c)

a, b, c, *d = 'ABCDEF'
print(a, b, c, d)

a, b, *c, d = 'ABCDEF'
print(a, b, c, d)

*a, b, c, d = 'ABCDEF'
print(a, b, c, d)

d = [2, 4, 6, 8]
print(*d, sep=':')

a = b = c = 0
a += 10
print(a, b, c)

a = b = c = {1, 2}
a.add(5)
print(a, b, c)

a, b, c, = 1, 2, 3
print(a, b, c)

t = 1, 2, 3
print(t, type(t))

