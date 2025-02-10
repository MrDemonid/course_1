d = {'one': 1, 'two': 2, 'ten': 4}

for i in d:
    print(i)

for i in d.values():
    print(i, end=", ")
print()

for (k, v) in d.items():
    print(k, v, end=";  ")
print()

k = {'six': 6, 'ten': 10}
d.update(k)
print(d)

d = {'one': 1, 'two': 2, 'ten': 4}
d |= {'six': 6, 'ten': 10}
print(d)

# n = d.pop('two')
# print(n)
# print(d)


# l = list(d.values())
# print(l)
#
# l = list(d.items())
# print(l)
#
