# Промежуточная аттестация по Python (семинары)

Задача:

>В ячейке ниже представлен код генерирующий **DataFrame**, которая состоит всего из 1 столбца. Ваша задача перевести его в one **hot вид**. Сможете ли вы это сделать без **get_dummies**?

```python
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
```

