# Итераторы

d = [1, 2, 3, 4, 5 ,6]

lt = iter(d)
print(next(lt))
print(next(lt))
print(*lt)


lt = iter(d)
while True:
    n = next(lt, None)
    if n is None:
        break
    print(n, end=' ')
print()


data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)
y = next(x)
print(y)
z = next(iter(y))
print(z)
