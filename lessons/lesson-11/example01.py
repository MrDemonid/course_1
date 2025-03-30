# __new__(class, *args, **kwargs)

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'создал {self.name}')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'-- создал класс {cls}')
        return instance


u_1 = User('Иван')
u_2 = User('Марья')
# -- создал класс <class '__main__.User'>
# создал Иван
# -- создал класс <class '__main__.User'>
# создал Марья
