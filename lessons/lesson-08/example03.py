import json

# Сериализация словаря и списка:
obj = {
    "userId": 1,
    "name": "Иван",
    "colors": {
        "head": "желтый",
        "body": "синий"
    },
    "hits": [1, 2, 3]
}
obj1 = {
    "userId": 2,
    "name": "Сергей",
    "colors": {
        "head": "красный",
        "body": "бежевый"
    },
    "hits": [4, 5, 6]
}

lst = [obj, obj1]


with open('./datas/ex3b.json', 'w', encoding='utf-8') as f:
    json.dump(lst, f)

# сохраняем объект без экранирующих символов
with open('./datas/ex3.json', 'w', encoding='utf-8') as f:
    json.dump(obj, f, ensure_ascii=False)


# проверяем:
with open('./datas/ex3.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
print(type(res))
print(res)
