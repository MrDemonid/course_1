with open('./datas/data03.txt', 'wt', encoding='utf-8') as f:
    f.writelines(['red\n', 'green\n', 'blue\n'])

# чтение целиком в список
with open('./datas/data03.txt', 'r', encoding='utf-8') as f:
    l = list(f)
    print(l)
print('-----------')

# через read()
with open('./datas/data03.txt', 'r', encoding='utf-8') as f:
    while res := f.read(8):         # читаем пока не вернет пустую строку
        print(res, end=" : ")
print('\n-----------')

# через readline()
with open('./datas/data03.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res, end='')
print('\n-----------')

with open('./datas/data03.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(4):
        print(res, end='.')
print('\n-----------')

# через for
with open('./datas/data03.txt', 'r', encoding='utf-8') as f:
    for l in f:
        print(l, end='')
print('\n-----------')

# убираем символы переноса строк в их конце
with open('./datas/data03.txt', 'r', encoding='utf-8') as f:
    for l in f:
        print(l[:-1])


