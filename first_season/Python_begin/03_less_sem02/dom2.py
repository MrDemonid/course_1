x = 1
y = s-1

while (x <= y):
    if (x * y) == p:
        break
    x += 1
    y -= 1

if (x < y):
    print(x, y)
else:
    print(y, x)

