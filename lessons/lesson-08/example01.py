import json

# Десериализация. JSON -> Python
with open('./datas/ex1.json', 'r', encoding='utf-8') as f:
    res = json.load(f)

print(f'{type(res) = }\n{res = }')
print(f'{res["name"] = }')
print(f'{res["address"]["geo"] = }')
print(f'{res["email"] = }')
print(res['fore'])
print(res['back'])
