pi = 3.141_592_148

print(f"Пи = {pi:.2f}")
print(f"Пи = {pi:>10}")
print(f"Пи = {pi:<10}end")
print(f"Пи = {pi = :_}")
print(f"Пи = {10000 = :_}")

print("v = {0} / {1}".format(30, 10))

# a, b, *c = input("введите два значения: ").split(' ')
# print(a, b, c)

# Функции строк
s = 'Съешь еще булок'


print(len(s))
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())

print(s.find("еще", 5, -1))
print(s.find("еще"))
print(s.rfind('е'))
print(s.startswith('Съ'))
print(s.rfind('f', 0, -8))

print(s.expandtabs(2))

print(" ".join(['1', '2', 'Ok']))
print(", ".join(('1', '5', 'No')))
print("; ".join({'1', '8', 'Yes'}))
print("/".join({'one': 1, 'two:': 2}))

print(s.split())
print(s.split('е'))
print(s.split(' ', 1))

print(s.count('е'))
print(s.count('е', 6, -1))

s = 'pen'
print(s.center(8))
print(s.center(8, '.'))
print(s.ljust(8))
print(s.ljust(8, '*'))
print(s.rjust(8))
print(s.rjust(8, '^'))
print("12".zfill(8))



