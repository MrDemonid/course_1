import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_csv('sample_data/california_housing_train.csv', sep=';')
df = pd.read_csv('california_housing_train.csv',sep=',')
# print(df.head(n=5))
# print(df.tail())
# print(df.shape)
# print(df.isnull())
# print(df.isnull().sum())
# print(df.dtypes)
# print(df.columns)

# # Выборка данных

# print(df['longitude'])                # один столбец
# print(df[['longitude', 'latitude']])    # два столбца

""" 
Задача. 
    Вывести столбец 'total_rooms', у которого медианный возраст 
    здания ('housing_median_age') меньше 20.
"""
# print(df[df['housing_median_age'] < 20])    # вывод строк, для которых df['housing_median_age'] < 20] == True
# # собственно вывод данных из столбца 'total_rooms', если df['housing_median_age'] < 20] == True
# print(df[df['housing_median_age'] < 20]['total_rooms'])    

# # несколько условий и столбцов
# print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)]['total_rooms'])    
# print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][['total_rooms','longitude','latitude']])

'''
    Простая статистика
'''
# print(df['longitude'].max())                # максимальное значение столбца(-ов)
# print(df[['longitude','latitude']].max())   # максимальное значение столбца(-ов)
# print(df['longitude'].min())                # минимальное  значение столбца(-ов)
# print(df['longitude'].mean())               # среднее  значение столбца(-ов)
# print(df['longitude'].median())             # медианное значение столбца(-ов)
# print(df['longitude'].count())              # количество непустых строк
# print(df['longitude'].sum())                # сумма всх элементов столбца(-ов)
# print(df['longitude'].std())                # стандартное отклонение от среднего значения

# # получить сводную информацию по столбцам (count, mean, std, min, max и Перцентиль(25%, 50%, 75%))
# print(df['longitude'].describe())  # получить всё информацию о столбце(-ах) 
# print(df.describe())               # получить всё информацию о таблице в целом

# # изобразим графически точки долготы по отношению к широте
# sns.scatterplot(data=df, x='longitude', y='latitude')
# plt.show()

# # изобразим отношения количества семей, количества людей и комнат
# sns.scatterplot(data=df, x='households', y = 'population', hue = 'total_rooms')
# plt.show()

# # то же самое, но с заданным размером точек
# sns.scatterplot(data=df, x='households', y = 'population', hue = 'total_rooms', size=10)
# plt.show()

# # Можно визуализировать сразу несколько отношений, используя класс PairGrid внутри seaborn.
# cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# plt.show()


# # Линейные графики.
# sns.relplot(data=df, x='latitude', y='median_house_value', kind = 'line')
# plt.show()
# sns.relplot(data=df, x='longitude', y='median_house_value', kind = 'line')
# plt.show()


# # Гистограммы.
# sns.histplot(data=df, x = 'median_income')
# sns.histplot(data=df, x = 'housing_median_age')
# plt.show()

# средний доход пожилых жителей
# sns.histplot(data=df[df['housing_median_age'] > 50], x = 'median_income')
# plt.show()


# # Разобьём возрастные категории на три группы, создав новый столбец в таблице:
# df.loc[df['housing_median_age'] < 20, 'age_group'] = 'Молодые'
# df.loc[(df['housing_median_age'] >= 20) & (df['housing_median_age'] <=50), 'age_group'] = 'Ср. возраст'
# df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
# print(df.columns)       # появился новый столбец 'age_group'
# print(df.head(10))      # в котором указывается тип возраста (Молодые, Ср. возраст и Пожилые)

# # сгруппируем и сразу построим график по среднему значению доходов
# df.groupby('age_group')['median_income'].mean().plot(kind = 'bar')
# plt.show()

# # разобьём на группы по среднему доходу
# df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
# df.loc[df['median_income'] <= 6, 'income_group'] = 'everyone_else'

# # и посмотрим на графике распределение доходов
# sns.histplot(data=df, x = 'median_house_value', hue='income_group')
# plt.show()

