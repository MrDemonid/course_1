k = tuple((1, 2, 3, 'Ok'))
print(k)

k = tuple()
print(k)


k = (1, 2, 3, 4, 5)
a, b, c, *_ = k
print(a, b, c)

k = (1, 2, 3, 4, 5)
a, b, c, *_ = k
print(a, b, c, _)

k = (1, 2, 3, 4, 5)
a, b, *c = k
print(a, b, c)


n = 65535.1256
k = 18
print(f'{n = }, {k = }')
print(f'{n = :_}')
print(f'{n:.2f}')
print(f'{k:>4}')
print(f'{k:<4}ru')
print('v = {1} / {0}'.format(1, 2))
print('v = {} / {}'.format(1, 2))


