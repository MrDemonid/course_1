""" 
    Метод №1.  Через loc[]
"""

import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

#=============================================================================

data = pd.DataFrame({'whoAmI': lst})    # изначальная таблица с одним столбцом

cols = list(set(data['whoAmI']))        # получаем список всех значений столбца

# добавляем в исходную таблицу столбцы и заполняем их значениями (0, 1)
for i in cols:
    data.loc[data['whoAmI'] == i, i] = 1
    data.loc[data['whoAmI'] != i, i] = 0
# последний этап: создаём отдельную таблицу one hot
onehot = data[cols]
onehot[cols] = onehot[cols].astype('uint8')         # по дефолту тип столбцов будет float, поэтому меняем его на int
print(onehot)                                       # получившаяся one hot таблица




# t = pd.get_dummies(data['whoAmI'], dtype=int)     # без dtype тип будет BOOL!!! (на gogle colab - uint8!!!)
# print(t) # таблица через get_dummies()
# print(t.dtypes)
