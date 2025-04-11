class FIO:
    """ Дескриптор для ФИО """

    cyrillic = set("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    latin = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self                         # обращение к дескриптору через класс
        return getattr(instance, self.name)     # обращение через экземпляр класса

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"Значение '{value}' должно быть строкой!")

        parts = value.strip().split()
        if not (1 <= len(parts) <= 3):
            raise ValueError("ФИО должно содержать от 1 до 3 слов!")

        for part in parts:
            if not (part.isalpha() and part[0].isupper() and part[1:].islower()):
                raise ValueError(
                    "Каждая часть ФИО должна начинаться с заглавной буквы и содержать только буквы!")

        if not self.is_cyrillic(parts) and not self.is_latin(parts):
            raise ValueError("ФИО должно состоять только из кириллических, или только из латинских букв!")
        setattr(instance, self.name, value)

    def is_cyrillic(self, text: [str]):
        ''' Проверка, что в тексте только символы кириллицы '''
        for string in text:
            if not all(ch in self.cyrillic for ch in string):
                return False
        return True

    def is_latin(self, text: [str]):
        ''' Проверка, что в тексте только символы латиницы '''
        for string in text:
            if not all(ch in self.latin for ch in string):
                return False
        return True
