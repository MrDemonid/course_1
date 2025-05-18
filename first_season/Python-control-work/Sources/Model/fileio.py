'''
    Класс для сохранение и загрузки CSV-файлов
'''

import csv
from Model.note import *
from Model.noteitem import *


class FileCSV:

    _fileName: str

    def __init__(self, fileName: str):
        self._fileName = fileName

    
    def load(self) -> Note:
        res = Note()
        with open(self._fileName, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for elem in reader:
                rec = NoteItem()
                if rec.setData(elem):
                    res.add(rec)
                else:
                    print(f'- Error: bad line: {elem}')
        # # сортирум по дате и уходим
        # res.sort()
        return res
    
    
    def save(self, note: Note):
        with open(self._fileName, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=list(note.get(0).getData().keys()), quoting=csv.QUOTE_ALL, delimiter=';', lineterminator="\n")
            writer.writeheader()
            for elem in note:
                rec = elem.getData()
                rec['date'] = elem.dateToStr()
                writer.writerow(rec)

