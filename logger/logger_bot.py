import logging
import os

name='DataBase'

# logging.basicConfig(level='DEBUG', filename='my_log.log')
debug_mode = False

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_DataBase.log")

# Создание объекта обработчика, который будет записывать логи в файл
file_handler = logging.FileHandler(log_file_path)
cons_handler = logging.StreamHandler()

# Установка уровней логирования для обработчиков
file_handler.setLevel(logging.WARNING)
cons_handler.setLevel(logging.DEBUG)

# Создание форматтера, определяющего, как будут выглядеть записи логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
cons_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(file_handler)
if debug_mode:
    logger.addHandler(cons_handler)
# lg = logging.getLogger('aiogram').setLevel('WARNING')







