# import logging
# import os
#
# name='DataBase'
#
# # logging.basicConfig(level='DEBUG', filename='my_log.log')
# debug_mode = False
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_DataBase.log")
#
# # Создание объекта обработчика, который будет записывать логи в файл
# file_handler = logging.FileHandler(log_file_path)
# cons_handler = logging.StreamHandler()
#
# # Установка уровней логирования для обработчиков
# file_handler.setLevel(logging.WARNING)
# cons_handler.setLevel(logging.DEBUG)
#
# # Создание форматтера, определяющего, как будут выглядеть записи логов
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# file_handler.setFormatter(formatter)
# cons_handler.setFormatter(formatter)
#
# # Добавление обработчиков к логгеру
# logger.addHandler(file_handler)
# if debug_mode:
#     logger.addHandler(cons_handler)
# # lg = logging.getLogger('aiogram').setLevel('WARNING')

import os
import logging
from logging.handlers import RotatingFileHandler

name='DataBase'
debug_mode = False

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание объекта обработчика, который будет записывать логи в файл с ограничением по размеру
log_file_path_info = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_DataBase_info.log")
backup_count_info = 5
max_log_size_info = 1024*1024*2
file_handler_info = RotatingFileHandler(log_file_path_info, maxBytes=max_log_size_info, backupCount=backup_count_info, encoding='utf-8')

log_file_path_error = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_DataBase_error.log")
backup_count_error = 2
max_log_size_error = 1024*1024*3
file_handler_error = RotatingFileHandler(log_file_path_error, maxBytes=max_log_size_error, backupCount=backup_count_error, encoding='utf-8')

# Установка уровней логирования для обработчиков
file_handler_info.setLevel(logging.INFO)
file_handler_error.setLevel(logging.ERROR)
# Создание форматтера, определяющего, как будут выглядеть записи логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler_info.setFormatter(formatter)
file_handler_error.setFormatter(formatter)


# Добавление обработчика к логгеру
logger.addHandler(file_handler_info)
logger.addHandler(file_handler_error)
if debug_mode:
    cons_handler = logging.StreamHandler()
    cons_handler.setLevel(logging.DEBUG)
    cons_handler.setFormatter(formatter)
    logger.addHandler(cons_handler)






