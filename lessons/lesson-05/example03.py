# Генераторы

gen = (chr(i) for i in range(97, 102))
print(gen)
for ch in gen:
    print(ch, end=' ')
print()

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res) = }')
print(res)
