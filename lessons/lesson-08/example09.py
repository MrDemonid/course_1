import pickle

def foo(a, b):
    return a + b

obj = {
    "userId": 1,
    "name": "Иван",
    "colors": {
        "head": "желтый",
        "body": "синий"
    },
    "hits": [1, 2, 3],
    "functions": (foo, sum, min, max),
    "bools": {True, False, 'Unknown'}
}

# Сериализация в bytes
res = pickle.dumps(obj, protocol=pickle.DEFAULT_PROTOCOL)
print(type(res))
print(res)


# Сериализация в бинарный файл
with open('./datas/ex9.bin', 'wb') as f:
    pickle.dump(obj, f)

