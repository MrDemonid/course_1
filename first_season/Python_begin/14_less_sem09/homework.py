import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv',sep=',')

""" 
Задача 40: 
    Работать с файлом california_housing_train.csv, который находится в папке
    sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
"""
# print('min cost: ', df[df['population'] <= 500]['median_house_value'].min())
# print('max cost: ', df[df['population'] <= 500]['median_house_value'].max())
# print('medium cost: ', df[df['population'] <= 500]['median_house_value'].mean())



""" 
Задача 42: 
    Узнать какая максимальная households в зоне минимального значения population
"""
print(df['population'].min())

print(df[df['population'] == df['population'].min()]['households'])
print(df[df['population'] == df['population'].min()]['households'].max())
