# Дендеры математики и логики.


class Closet:
    CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли', 'платок', 'галстук', 'свитер')

    def __init__(self, count: int, storeroom=None):
        self.count = count if count <= len(self.CLOTHES) else len(self.CLOTHES)
        if storeroom is None:
            self.storeroom = self.CLOTHES
        else:
            self.storeroom = storeroom

    def __str__(self):
        names = ', '.join(self.storeroom)
        return f'Осталось вещей в шкафу {self.count}: {names}'

    def __rshift__(self, other):
        shift = self.count if other > self.count else other
        self.count -= shift
        return Closet(self.count, self.storeroom[:self.count])


storeroom = Closet(10)
print(storeroom)
for _ in range(4):
    storeroom = storeroom >> 3
    print(storeroom)

# Осталось вещей в шкафу 10: брюки, рубашка, костюм, футболка, перчатки, носки, туфли, платок, галстук, свитер
# Осталось вещей в шкафу 7: брюки, рубашка, костюм, футболка, перчатки, носки, туфли
# Осталось вещей в шкафу 4: брюки, рубашка, костюм, футболка
# Осталось вещей в шкафу 1: брюки
# Осталось вещей в шкафу 0:

print('---------------------')


class StrPro(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __rmul__(self, other: str):
        words = other.split()
        result = self.join(words)
        return StrPro(result)


text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')
print(text * s)
# print(s * text)  # TypeError: 'str' object cannot be interpreted as an integer

# text = 'Каждый охотник желает знать где сидит фазан'
# s = ' (=^.^=) '
# Каждый (=^.^=) охотник (=^.^=) желает (=^.^=) знать (=^.^=) где (=^.^=) сидит (=^.^=) фазан

print('----------------------------')

from decimal import Decimal


class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'

    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self


m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)

# Money(100.00)
# Money(150.00)
# Money(300.00)
