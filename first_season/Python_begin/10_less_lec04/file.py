colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')        # здесь указываем режим, в котором будем работать
# data = open('file.txt', 'a', encoding='utf-8')        # здесь указываем режим, в котором будем работать
data.writelines(colors)     # записалось: redgreenblue
data.close()

with open('file.txt', 'w') as f:
    f.write('line 1\n')
    f.write('line two\n')
# теперь в файле:
# line 1
# line two

# читаем из файла
f = open('file.txt', 'r')
for line in f:
    print(line)
f.close()

