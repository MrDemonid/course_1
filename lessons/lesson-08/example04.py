import json


# Сериализация в строку с JSON-структурой

obj = {
    "userId": 1,
    "name": "Иван",
    "colors": {
        "head": "желтый",
        "body": "синий"
    },
    "hits": [1, 2, 3]
}


s = json.dumps(obj)
t = json.dumps(obj, ensure_ascii=False)
print(type(s))
print(s)
print(t)


