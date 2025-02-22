# Генераторы списков, множеств и словарей

l = [chr(i) for i in range(97, 102)]
print(l)

l = {chr(i) for i in range(97, 102)}
print(l)

l = {i: chr(i) for i in range(97, 102)}
print(l)

# условие с ELSE
d = [1, 2, 3, 3, 4]
l = [i if i % 2 != 0 else (i / 10) for i in d]
print(l)


data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1)
print(res2)
print(res3)


