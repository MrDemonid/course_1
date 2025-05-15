# Вывод даты в разных форматах

from datetime import datetime


dt = datetime(2007, 12, 21, 2, 14, 0, 24)
print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))


# Ввод даты в разных форматах

original_date = datetime.fromisoformat('2022-12-12 18:01:21.555470')
iso_date = datetime.fromisoformat('2007-06-15T02:14:00.000024')
timestamp_date = datetime.fromtimestamp(1181862840.000024)
date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')
print(original_date)
print(iso_date)
print(timestamp_date)
print(text_date)
