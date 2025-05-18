""" 
    Метод №3. По семинару (метод без loc[]).
    (хотя если создавать столбцы как это было на семинаре, то пайтон ругается 
    и предлагает использовать loc[] (но всё же создаёт столбцы))
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
onehot = pd.DataFrame()                 # пустая таблица, нужна для начального задания типа

cols = list(set(data['whoAmI']))        # получаем список всех значений столбца

# добавляем в таблицу one_hot столбцы и заполняем их значениями (True/False)
for i in cols:
    onehot[i] = data['whoAmI'] == i

onehot = onehot.astype('uint8')         # по дефолту тип столбцов будет bool, поэтому меняем его на int
print(onehot)                           
# print(data)
