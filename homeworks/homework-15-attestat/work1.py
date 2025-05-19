"""
Задание 1. Логирование с использованием нескольких файлов.

Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.
"""
import logging


FORMAT = '{levelname} [{asctime}] {name}: {msg}'


def create_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET)
    return logger


def create_logger_handler(fn, level):
    handler = logging.FileHandler(filename=fn, mode='w', encoding='utf-8')
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(fmt=FORMAT, style='{'))
    return handler


log = create_logger()
log.addHandler(create_logger_handler("debug_info.log", logging.DEBUG))
log.addHandler(create_logger_handler("warnings_errors.log", logging.WARNING))

log.log(logging.NOTSET, "We have a NOTSET")
log.debug("We have a DEBUG")
log.info("We have a INFO")
log.warning("We have a WARNING")
log.error("We have a ERROR")
log.fatal("We have a FATAL")
log.critical("We have a CRITICAL")
