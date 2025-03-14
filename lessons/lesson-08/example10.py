import pickle


# Десериализация

def foo(a, b):
    return a * b


with open('./datas/ex9.bin', 'rb') as f:
    res = pickle.load(f)

print(res)
print(res['hits'])
print(res["functions"][0](4, 9))  # foo(4, 9)


