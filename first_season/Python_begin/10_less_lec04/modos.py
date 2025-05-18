import os

p = os.getcwd() + '\\file.txt'
print(f'"{p}"')

fname = os.path.basename(p)
print(fname)
fpath = os.path.abspath('file.txt')
print(fpath)

