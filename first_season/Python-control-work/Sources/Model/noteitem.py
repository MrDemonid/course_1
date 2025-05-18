'''
    Класс для хранения и работы с одной записью 
'''

from datetime import date
import datetime


class NoteItem(object):
    
    _id: int
    _title: str                     # заголовок
    _body: str                      # тело записи
    _datetime: datetime.datetime    # дата и время создания/изменения записи 

    def __init__(self, id = None, title = None, body = None, data=datetime.datetime.today()):
        self._id = id
        self._title = title
        self._body = body
        self._datetime = data

    @property
    def id(self):
        return self._id

    def setData(self, rec: dict) -> bool:       # добавляет данные в формате словаря
        try:
            if rec['title'] == '' or rec['note'] == '':
                return False
            self._id = int(rec['id'])
            self._datetime = self.strToDate(rec['date'].strip())
            self._title = str(rec['title']).strip()
            self._body = str(rec['note']).strip()
        except ValueError:
            return False
        return True


    def getData(self) -> dict:                  # возвращает данные в формате словаря
        res = {}
        try:
            res['id'] = self._id
            res['title'] = self._title
            res['note'] = self._body
            res['date'] = self._datetime
        except ValueError:
            res = {}
        return res


    def dateToStr(self) -> str:
        return f'{self._datetime.day:02d}.{self._datetime.month:02d}.{self._datetime.year} {self._datetime.hour:02d}:{self._datetime.minute:02d}:{self._datetime.second:02d}'


    def strToDate(self, dt: str) -> datetime.datetime:
        return datetime.datetime.strptime(dt, '%d.%m.%Y %H:%M:%S')


    def toString(self) -> str:
        return f'[{self._id}]: {self._title} от {self.dateToStr()}\n{self._body}\n'
    
    #########################################################################
    # Методы для удобного сравнения объектов и конвертации в строковой формат
    #
    def __eq__(self, obj):                      # if rec == obj
        if obj is None:
            return False
        return self._id == obj.id
    
    def __ne__(self, obj):                      # if rec != obj
        if obj is None:
            return False
        return self._id != obj.id
    
    def __lt__(self, other):                    # list(recs).sort()
        return self._id < other._id
        # return self._datetime < other._datetime
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:                   # str(rec)
         return self.toString()
    
    def __repr__(self) -> str:                  # print(rec)
        return self.toString()
           
    
    # @property
    # def title(self) -> str:
    #     return self._titleRec
    
    # @title.setter
    # def title(self, new_title: str) -> str:
    #     self._titleRec = new_title
    #     return self._titleRec

    