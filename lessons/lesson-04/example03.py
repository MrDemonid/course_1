# лямбды

d = {'two': 2, 'one': 1, 'four': 4}


def foo(x: tuple):
    return x[1]

sk = sorted(d.items())
sv = sorted(d.items(), key=lambda x: x[1])
sn = sorted(d.items(), key=foo)

print(sk)
print(sv)
print(sn)


# выбрать из списка чётные данные и возвратить пары: число и его квадрат
l = [1, 2, 3, 4, 5, 6 ,7, 8]

def where(lst, op):
    return [(i, i*i) for i in lst if op(i)]

res = where(l, lambda n: n % 2 == 0)
print(res)

# создать "макрос" выбора максимального числа
_max = lambda a, b: a if a > b else b

print(_max(12, 8))
