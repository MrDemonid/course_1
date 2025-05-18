""" 
    Метод №2. 
    Через создание словаря.
    Здесь нам вообще не нужно создавать изначальную таблицу, сразу one hot.    
"""

import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

#===============================================================================

cols = list(set(lst))                   # получаем список всех значений столбца
# создаём словарь
res = dict()
for n in cols:
    res[n] = [1 if i == n else 0 for i in lst]

# переводим словарь в таблицу
pf = pd.DataFrame(res)
pf[cols] = pf[cols].astype('uint8')     # меняем float на uint8, как это делается в google colab

print(pf)
