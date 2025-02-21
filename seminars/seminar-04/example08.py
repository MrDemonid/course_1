"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

companie = "source"
companies = "companies"
stack = "source"
stacks = "stacks"
tople = 12
toples = 100.0
s = ['Names', 122]


def replacement():
    var = globals().copy()
    for n, v in var.items():
        if len(n) > 1 and not n.startswith('__') and n.endswith('s'):
            globals()[n[:-1]] = v
            globals()[n] = None
    return globals().copy()

variables = replacement()
for i, v in variables.items():
    print(i, ': ', v)

globals()['stack'] = 'AUGHHH!!!!'       # меняем значение переменной stack
print(globals())
