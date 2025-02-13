d = {'one': 1, 'two': 2, 'ten': 4}

for i in d:
    print(i)

for i in d.values():
    print(i, end=", ")
print()

for (k, v) in d.items():
    print(k, v, end=";  ")
print()

print("\nupdates\n")
k = {'six': 6, 'ten': 10}
d = {'one': 1, 'six': 8}
d.update(k)
print(d)

d = {'one': 1, 'six': 8}
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
print("\nsetdefault\n")
d = {}
a = d.setdefault('red', 3)
b = d.setdefault('green')
c = d.setdefault('red', 8)

print(d)
print(a, b, c)
