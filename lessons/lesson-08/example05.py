import json

# параметры dump(s)

obj = {
    "userId": 1,
    "name": "Иван",
    "colors": {
        "head": "желтый",
        "body": "синий"
    },
    "hits": [1, 2, 3]
}

t = json.dumps(obj, ensure_ascii=False)
s = json.dumps(obj, ensure_ascii=False, indent=2, separators=(',', ': '), sort_keys=True)
print(t)
print(s)

with open('./datas/ex5.json', 'w', encoding='utf-8') as f:
    json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=True)

# Задание
# Перед вами несколько строк кода. Какой объект будет получен после его
# выполнения?
a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)
