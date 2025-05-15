# Математика с датами
from datetime import datetime, time, timedelta

date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(delta)

birthday = datetime(2022, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(new_date)


# Доступ к полям
print(f'{new_date.month = }')
print(f'{new_date.second = }')
print(f'{new_date.hour = }')
print(f'{dlt.days = }')


# Замена значений (у timedelta нет метода replace)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)
print(new_dt)
print(one_more_hour)

