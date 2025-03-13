import json

# Строка JSON -> Python
text = """
[
    {
        "userId": 1,
        "name": "Ivan",
        "color": {
            "head": "yellow",
            "body": "blue",
            "leg": "brown"
        },
        "hits": [
            1, 2, 3
        ]
    },
    {
        "userId": 2,
        "name": "Maria",
        "color": {
            "head": "magenta",
            "body": "red",
            "leg": "yellow"
        },
        "hits": [
            4, 5, 6
        ]
    },
    {
        "userId": 3,
        "name": "Lena",
        "color": 
        {
            "head": "cyan",
            "body": "green",
            "leg": "#8B29CD"
        },
        "hits": [
            7, 8, 9
        ]
    }
]
"""


res = json.loads(text)
print(type(res))
# print(res)
print(res[1])
print(res[1]["color"])
print(res[1]["color"]["body"])
print(res[1]["hits"][-1])
