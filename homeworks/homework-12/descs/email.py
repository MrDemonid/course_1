class Email:
    """ Дескриптор для мыла """

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self                         # обращение к дескриптору через класс
        return getattr(instance, self.name)     # обращение через экземпляр класса

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"Значение '{value}' должно быть строкой!")
        t = value.split("@")
        if len(t) != 2 or not "." in t[-1]:
            raise ValueError(f"Значение '{value}' не является электронной почтой!")
        setattr(instance, self.name, value)

