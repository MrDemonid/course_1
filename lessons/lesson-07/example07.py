import os
import shutil
from pathlib import Path

# текущий каталог
print(os.getcwd())
print(Path.cwd())


# Смена каталога
os.chdir("..")
print(os.getcwd())
os.chdir("./lesson-07")
print(os.getcwd())

# создание каталога
# os.mkdir('new_dir_os')
# Path('new_dir_pt').mkdir()

# создание каталога с вложениями
os.makedirs('new_d_os/sub_dir/sub_os')
Path('new_d_pt/sub_dir/sub_os').mkdir(parents=True)

# удаление каталога (последний в указанной цепочке)
os.rmdir('new_d_os/sub_dir/sub_os')
Path('new_d_pt/sub_dir/sub_os').rmdir()

# удаление каталога со всем содержимым
shutil.rmtree('new_d_os')
shutil.rmtree('new_d_pt')

# формирование пути
file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')

# список файлов и директорий
print(os.listdir())
# for obj in Path(Path().cwd()).iterdir():
#     print(obj)

# проверка на файл, директорию, ссылку
l = os.listdir()
for n in l:
    if os.path.isdir(n):
        s = 'directory'
    elif os.path.isfile(n):
        s = 'file'
    elif os.path.islink(n):
        s = 'link'
    else:
        s = 'unknown'
    print(f"{n = }", s)

p = Path(Path().cwd())
for n in p.iterdir():
    if n.is_dir():
        s = 'directory'
    elif n.is_file():
        s = 'file'
    elif n.is_symlink():
        s = 'link'
    else:
        s = 'unknown'
    print(f"{n = }", s)

# обход папок через walk()
