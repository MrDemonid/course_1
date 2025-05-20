# Модуль array

from array import array, typecodes


byte_array = array('B', (1, 2, 3, 255))
print(byte_array)
print(typecodes)


# методы аналогичные list
long_array = array('l', [-6000, 800, 100500])
long_array.append(42)
print(long_array)
print(long_array[2])
print(long_array.pop())


long_array = array('l', [-6000, 800, 100500])
long_array.append(2**32) # OverflowError: Python int too large to convert to C long
long_array.append(3.14) # TypeError: 'float' object cannot be interpreted as an integer
