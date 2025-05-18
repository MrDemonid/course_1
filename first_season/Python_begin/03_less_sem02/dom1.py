# coins = [0, 1, 0, 1,  0]

# Введите ваше решение ниже
nul = 0
for i in range(len(coins)):
    if coins[i] == 0:
        nul += 1

one = len(coins) - nul
if one < nul:
    print(one)
else:
    print(nul)
