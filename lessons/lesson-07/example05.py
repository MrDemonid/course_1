# текущая позиция в файле
l = ["red", "green", "blue"]

with open('./datas/data05.txt', 'w', encoding='utf-8') as f:
    for s in l:
        f.write(f'{s}')
        print(f.tell())


# seek
with open('./datas/data05.txt', 'r+', encoding='utf-8') as f:
    size = f.seek(0, 2)
    print("check", file=f)
    f.seek(size, 0)
    print("---no", file=f)


# truncate - изменение размера файла
with open('./datas/data05.txt', 'r+', encoding='utf-8') as f:
    size = f.seek(0, 2)
    print(size)
    f.seek(size-2, 0)
    f.truncate()            # обрезали 0x0D, 0x0A от прошлой записи

# расширяем до размера в 24 байта
with open('./datas/data05.txt', 'r+', encoding='utf-8') as f:
    f.truncate(24)


