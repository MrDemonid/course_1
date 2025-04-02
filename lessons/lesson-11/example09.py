# Атрибуты

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __getattribute__(self, item):
        if item in ['x', 'y']:
            return object.__getattribute__(self, item)
        raise AttributeError('Неизвестный атрибут: ' + item)

    def __getattr__(self, item):
        """ Перехватывает AttributeError от __getattribute__() """
        return None

    def __setattr__(self, key, value):
        if key in ['x', 'y', 'z']:
            print(f"set [{key} = {value}]")
            return object.__setattr__(self, key, value)
        raise AttributeError("Попытка присвоить новый атрибут")

    def __delattr__(self, item):
        if item in ['x', 'y']:
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)


a = Vector(2, 4)
print(f'{a = }')
print(a.x, a.y)
print(a.n)  # AttributeError: Неизвестный атрибут: n (если не определить __getattr__())
a.z = 12
print(a.z)  # вернет None, поскольку в __getattribute__() это поле вызовет ошибку!

del a.z
del a.x
print(a)
print(a.z)