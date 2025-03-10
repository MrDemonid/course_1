"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os

__DIR_VIDEO = './datas/ex7/videos'
__DIR_MUSIC = './datas/ex7/music'
__DIR_DOCS = './datas/ex7/docs'
__DIR_PICS = './datas/ex7/pics'
__DIR_TRACKERS = './datas/ex7/trackers-music'

__ext_videos = ('.mp4', '.avi', '.mov', '.dat')
__ext_musics = ('.mp3', '.wav')
__ext_trackers = ('.st3', '.xm', '.mod', '.mtm', '.hsc', '.rad', '.stc')
__ext_docs = ('.txt', '.doc', '.me', '.md', '.rtm', '.pdf', '.djvu', '.djv')
__ext_pics = ('.bmp', '.png', '.pic', '.jpg', '.jpeg', '.pcx', '.gif')

__roots = {__DIR_VIDEO: __ext_videos,
           __DIR_PICS: __ext_pics,
           __DIR_MUSIC: __ext_musics,
           __DIR_DOCS: __ext_docs,
           __DIR_TRACKERS: __ext_trackers}


def check_directories(*args: str):
    """ Проверка наличия директорий и создание в случае их отсутствия. """
    for d in args:
        if not os.path.isdir(d):
            os.makedirs(d)
            print(f"  - create directory {d}")


def sort_files(directory, roots: dict[str: tuple[str]]):
    if os.path.isdir(directory):
        print('Start sorting files to categories...')
        check_directories(*roots.keys())
        for name in os.listdir(directory):
            full = os.path.join(directory, name)
            if os.path.isfile(full):
                for k, v in roots.items():
                    s = os.path.splitext(name)[1].lower()
                    if s in v:
                        os.replace(full, os.path.join(k, name))
                        print(f"  - move file {full} -> {os.path.join(k, name)}")
                        break
    else:
        print(f"Error: directory {directory} is bad!")


if __name__ == '__main__':
    sort_files('./datas/ex7', __roots)
