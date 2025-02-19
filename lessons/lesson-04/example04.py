lst1 = []
lst2 = [42, 256, 73]
lst3 = [("Иван", 12), ("Пётр", 72), ("Оля", 29)]
print(max(lst1, default='empty'))
print(max(*lst2))
print(max(lst3, key=lambda n: n[1]))
print(min(lst3, key=lambda n: n[1]))

