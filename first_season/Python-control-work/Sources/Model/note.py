'''
    Класс для работы со списком записей
'''

from Model.noteitem import *


class Note:

    _items: list[NoteItem]          # список записей
    _id: int                        # хранит номер максимального id записей (для добавления последующих)

    def __init__(self):
        self._items = []            # инициализируем пустой список
        self._id = 1
        
    #
    #  Возвращает количество элементов в списке
    #
    def size(self):
        return len(self._items)
    
    @property
    def id(self):
        return self._id
    
    #
    #  Добавляет запись. Если запись с таким ID уже существует, то заменяет её на новую
    #
    def add(self, rec: NoteItem):
        if rec in self._items:
            # запись уже существует, меняем её
            index = self._items.index(rec)  
            self._items.pop(index)
            self._items.insert(index, rec)
        else:
            self._items.append(rec)
        # определяем свободный id
        if rec.id >= self._id:
            self._id = rec.id+1

    #
    # Возвращает запись по индексу в списке 
    #
    def get(self, index) -> NoteItem:
        if index < len(self._items):
            return self._items[index]
        return None
    
    #
    # Удаление записи
    #
    def delete(self, index) -> bool:
        if index < len(self._items):
            self._items.pop(index)
            return True
        return False


    #############################################
    # Методы для итератора и конвертации в строку
    #
    def __iter__(self):
        return NoteIterator(self._items)

    def __repr__(self) -> str:
        res = ''
        for elem in self._items:
            res = res + str(elem)
        return res
    

'''
    Класс для итерации списка NoteItem
'''
class NoteIterator:
    note: list[NoteItem]
    current: int

    def __init__(self, note):
        self.note = note
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.current < len(self.note)):
            res = self.note[self.current]
            self.current += 1
            return res
        
        raise StopIteration
    
