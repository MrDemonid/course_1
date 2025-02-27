import random as rnd

d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(rnd.random())

# state()
state = rnd.getstate()
print(rnd.random())
rnd.setstate(state)
print(rnd.random())
print(rnd.random())


for _ in range(10):
    print(rnd.randrange(9, 100, 3), end=', ')
print('\x08\x08')


# d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = [1, 2, 2, 3, 3, 3, 4, 4, 5]
c = [1, 1, 0, 1, 0, 0, 1, 0, 1]
print(rnd.sample(d, 4))
print(rnd.sample(d, 4, counts=c))

rnd.shuffle(d)
print(d)
