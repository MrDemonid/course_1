# менеджер контекста with open

with open('./datas/data02a.txt', 'wt', encoding='utf-8') as f:
    f.writelines(['red\n', 'green\n', 'blue\n'])

with open('./datas/data02b.txt', 'wt', encoding='utf-8') as f:
    f.writelines(['kr580\x8D\n', 'kp1254\n', 'kt315\n'])

with open('./datas/data02c.txt', 'wb') as f:
    f.writelines(['less\n'.encode('utf-8'), 'more\n'.encode('utf-8'), 'equals\n'.encode('utf-8')])


# старый вариант работы с несколькими файлами сразу
with open('./datas/data02a.txt', 'r', encoding='utf-8') as f1, \
        open('./datas/data02b.txt', 'r', encoding='utf-8', errors='backslashreplace') as f2, \
        open('./datas/data02c.txt', 'rb') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))

# новый вариант с версии 3.10
with (open('./datas/data02a.txt', 'r', encoding='utf-8') as f1,
        open('./datas/data02b.txt', 'r', encoding='utf-8', errors='backslashreplace') as f2,
        open('./datas/data02c.txt', 'rb') as f3):
    print("".join(f1.readlines()))
    print(list(f2))
    print(list(f3))


# ['red\n', 'green\n', 'blue\n']
# ['kr580\x8d\n', 'kp1254\n', 'kt315\n']
# [b'less\n', b'more\n', b'equals\n']
# red
# green
# blue
#
# ['kr580\x8d\n', 'kp1254\n', 'kt315\n']
# [b'less\n', b'more\n', b'equals\n']

