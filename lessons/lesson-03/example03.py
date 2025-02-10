import copy

l = [1, 2, [12, 13], -1]

# поверхностное копирование
t = l.copy()
l[2][1] = 0
print(t)

# полное копирование
t = copy.deepcopy(l)
l[2][1] = 13
print(l)
print(t)


