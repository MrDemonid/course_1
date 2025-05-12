# логирование в файл.

import logging


logging.basicConfig(filename='ex5.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')

# filename - имя файла
# filemode - режим записи ('w' - перезапись при старте, остутствие - дозапись в конец файла)
