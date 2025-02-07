t = list("Tuple")
l = [2, True, [3.14, "Pi"], (False, "Tuple")]
l.extend(t)
l.insert(2, 3)
print(l)
