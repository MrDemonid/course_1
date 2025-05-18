import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



""" 
Задача №63
1. Изобразите отношение households к population с помощью точечного графика
2. Визуализировать longitude по отношения к median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
"""
# df = pd.read_csv('california_housing_train.csv',sep=',')

# sns.scatterplot(data=df, x = 'households', y = 'population')
# sns.relplot(data=df, x='longitude', y = 'median_house_value')
# sns.histplot(data=df, x='housing_median_age', kind='line')
# sns.histplot(data=df, x = 'median_house_value', hue = 'housing_median_age')
# sns.distplot(data=df, x = 'median_house_value', hue = 'housing_median_age')
# plt.show()


""" 
Задача №65
Написать EDA для датасета про пингвинов
Необходимо:
1) Использовать 2-3 точечных графика
2) Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
3) Использовать PairGrid с типом графика на ваш выбор
4) Изобразить Heatmap
5) Использовать 2-3 гистограммы

'species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex'
            остров    длина клюва       глубина клюва    длина ласт           масса тела     пол (Male, Female)
              3       31.1 - 59.6       13.1 - 21.5      172.0-231.0           2700-6300
                         43.92             17.15            200.91               4201.7
"""
# pg = sns.load_dataset("penguins")
# # получаем все значения 'island'
# # seat = list(set(pg['island']))
# 
# cols = ['island','bill_length_mm','body_mass_g','flipper_length_mm', 'sex']
# g = sns.PairGrid(pg[cols])
# g.map(sns.scatterplot)
# plt.show()
# pg.groupby('island')['bill_length_mm'].mean().plot(kind='bar')
# plt.show()

# sns.histplot(data=pg, x='bill_length_mm', y='body_mass_g', hue='sex')
# plt.show()

""" 
Задача №67. Решение в группах
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
 """
df = sns.load_dataset("penguins")
# df.loc[df['bill_length_mm'] >= 42, "height_group"] = 'high'
# df.loc[(df['bill_length_mm'] >= 35) & (df['bill_length_mm'] < 42), "height_group"] = 'middle'
# df.loc[df['bill_length_mm'] < 35, "height_group"] = 'low'
# print(df.head(30))

df[df['bill_length_mm'] >= 42]['height_group'] = 'high'
df[df['bill_length_mm'] < 35]['height_group'] = 'low'
df[(df['bill_length_mm'] >= 35) & (df['bill_length_mm'] < 42)]['height_group'] = 'middle'
print(df.head(30))

""" 
Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ
 """
# df = sns.load_dataset("penguins")
# sns.displot(data=df, x = 'flipper_length_mm', hue='height_group')
# plt.show()

