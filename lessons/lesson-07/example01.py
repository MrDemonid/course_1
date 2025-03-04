# создаем файл с разными кодировками

f = open("./datas/data01.txt", mode='wb')
f.write("Привет, ".encode('utf-8') + "мир".encode('cp1251'))
f.close()

# ['Привет, ���']
f = open("./datas/data01.txt", 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()

# ['Привет, ���']
f = open("./datas/data01.txt", 'r', encoding='utf-8', errors='replace')
l = f.readlines()
print(l)
f.close()

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
f = open("./datas/data01.txt", 'r', encoding='utf-8')
for s in f:
    print(s)
f.close()

