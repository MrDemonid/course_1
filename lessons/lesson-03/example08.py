text = "Привет"
res = text.encode('utf-8')
print(type(res), res)

text = "Hello"
res = text.encode('utf-8')
print(type(res), res)

n = bytearray("Hello".encode('utf-8'))
n.append(0x21)
print(n)


