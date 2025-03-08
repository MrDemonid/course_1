import os
from pathlib import Path
import shutil

# переименование файла
os.rename('./datas/old.bin', 'datas/new.bin')

p = Path('./datas/new.bin')
p.rename('./datas/old.bin')


# перемещение файла
os.replace('./datas/old.bin', os.path.join(os.getcwd(), 'datas', 'sub', 'new.bin'))

p = Path(Path.cwd() / 'datas' / 'sub' / 'new.bin')
nfile = p.replace(Path.cwd() / 'datas' / 'old.bin')


# копирование файлов
shutil.copy('./datas/old.bin', './datas/vxd')
shutil.copy2('./datas/old.bin', './datas/sub')      # копируем содержимое с метаданными

# копирование каталога
shutil.copytree('./datas/vxd', './datas/new-vxd')
shutil.rmtree('./datas/new-vxd')       # подчищаем, а то потом вызов приведет к ошибке


# удаление файла

os.remove('./datas/vxd/old.bin')
Path('./datas/sub/old.bin').unlink()
