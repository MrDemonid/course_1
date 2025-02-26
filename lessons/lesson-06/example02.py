# Псевдонимы
#
import random as rnd
from sys import path, builtin_module_names as bmn

print(rnd.randint(1, 6))
print(bmn)
print(*path, sep='\n')

