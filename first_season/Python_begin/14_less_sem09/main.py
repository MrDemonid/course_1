import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv',sep=',')

""" 
Задача №57
1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""
# print(f'Строк и столбцов: {df.shape}')
# print(f'Типы столбцов: \n{df.dtypes}')



""" 
Задача №59
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
 """
# print((df.isnull().sum()).sum())

# print(df[df['median_income'] < 2]['median_house_value'])

# print(df[['longitude', 'latitude']])
       
# print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])


""" 
Задача №61
1. Определить какое максимальное и минимальное значение median_house_value
2. Показать максимальное median_house_value, где median_income = 3.1250
3. Узнать какая максимальная population в зоне минимального значения median_house_value
"""
# print(f'min: {df['median_house_value'].min()}\nmax: {df['median_house_value'].max()}')

# print(df[df['median_income'] == 3.1250]['median_house_value'].max())

# print(df[df['median_house_value'] == df['median_house_value'].min()])
print(df[df['median_house_value'] == df['median_house_value'].min()]['population'].max())
