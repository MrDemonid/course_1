# Модуль collectoins.

from collections import namedtuple
from datetime import datetime
from time import sleep

User = namedtuple('User', ['fname', 'lname', 'birthday'])
u = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u)
print(type(User), type(u))

print(u.fname, u.lname)
print(u.birthday.year)


# Значения по умолчанию.
User = namedtuple('User', ['fname', 'lname', 'birthday'], defaults=['Иванов', datetime.now()])
u1 = User('Исаак')
print(u1.fname, u1.lname, u1.birthday.strftime("%H:%M:%S"))
sleep(7)
u2 = User('Галилей', 'Галилео')
print(u2.fname, u2.lname, u2.birthday.strftime("%H:%M:%S"))

