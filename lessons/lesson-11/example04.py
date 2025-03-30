# Приоритет __str__() и __repr__()

class User:
    def __init__(self, name,  equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []

    def simple_method(self):
        self.name.capitalize()

    def __str__(self):
        return f'Экземпляр User с именем "{self.name}"'

    def __repr__(self):
        return f'User("{self.name}", {self.equipment})'

user = User('Спенглер', ['рогатка', 'ловушка'])

print(user)             # __str__()
print(f'{user}')        # __str__()

print(repr(user))       # __repr__()
print(f'{user = }')     # __repr__()

# Экземпляр User с именем "Спенглер"
# Экземпляр User с именем "Спенглер"
# User("Спенглер", ['рогатка', 'ловушка'])
# user = User("Спенглер", ['рогатка', 'ловушка'])
print('------------------------')

u1 = User("Петя", ["лук"])
u2 = User("Маша", ["кукла", "книжка"])
lst = [u1, u2]

print(lst)
print(f"{lst}")
print(*lst, sep=" | ")

# [User("Петя", ['лук']), User("Маша", ['кукла', 'книжка'])]
# [User("Петя", ['лук']), User("Маша", ['кукла', 'книжка'])]
# Экземпляр User с именем "Петя" | Экземпляр User с именем "Маша"
