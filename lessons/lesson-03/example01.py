t = list("Tuple")
l = [2, True, [3.14, "Pi"], (False, "Tuple")]
l.extend(t)
l.insert(2, 3)
print(l)


l = [ch for ch in "abone 991" if ch.isdigit()]
print(l)

k = list("Ok")
l.extend(k)
print(l)