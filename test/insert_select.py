# from DataBaseApi.DB.DB_manager import DB_connector
# import time
#
#
# def get(name_table, get_dict):
#     name_tabl = name_table
#     response_by_db = DB_connector.get(name_table=name_tabl, **get_dict )
#     if not response_by_db:
#         print(response_by_db)
#
# def set(name_table, post_dict):
#     name_tabl = name_table
#     response_by_db = DB_connector.set(name_table=name_tabl, **post_dict)
#     if not response_by_db:
#         print(response_by_db)
#
#
#
#
# # name_table = "stop_work"
# # set_dict = {
# # 'city': 'Липецк',
# # 'object': 'Зверево',
# # 'position': '1',
# # 'queue': '1',
# # 'number_bk': '1',
# # 'cause_stop': 'погода',
# # 'user_id_stop_work': '1234',
# #
# # }
# # post_dict = {'set_dict': set_dict}
# # start_set_time = time.time()
# # for x in range(1, 100001):
# #     set(name_table, post_dict)
# # end_set_time = time.time()
# # execution_set_time = end_set_time - start_set_time
# # print(f"Время выполнения приложения set: {execution_set_time} секунд")
#
#
# # name_columns_tuple = ('id', 'city')
# # where_dict = {'city': 'Липецк'}
# # get_dict = {
# # 'name_columns_tuple': name_columns_tuple,
# # 'where_dict': where_dict
# # }
# #
# # start_get_time = time.time()
# # for x in range(1, 1001):
# #     get(name_table, get_dict)
# #     print(x)
# # end_get_time = time.time()
# # execution_get_time = end_get_time - start_get_time
# # print(f"Время выполнения приложения get: {execution_get_time} секунд")


import os
import time

from dotenv import load_dotenv
import asyncio
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from DataBaseApi.DB.Table_classes import Base, all_table_dict
from logger.logger_bot import logger

load_dotenv()
POSTGRESQL_URL_FOR_ENGINE = os.getenv('POSTGRESQL_URL_FOR_ENGINE')

# Создаем асинхронный движок
engine = create_async_engine(POSTGRESQL_URL_FOR_ENGINE, echo=False, future=True)

# Создаем базовый класс для объявления моделей
Base = declarative_base()

# Определяем асинхронную сессию
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Функция для асинхронной записи в базу данных
async def set(name_table: str, set_dict: dict) -> bool:
    async with async_session() as session:
        new_row = all_table_dict.get(name_table)(**set_dict)
        try:
            session.add(new_row)
            await session.commit()
            return True
        except Exception as ex:
            logger.error(f'data did not save to DB\n{ex}')
            print(f'data did not save to DB\n{ex}')
            return False
async def get(name_table: str, name_columns_tuple: tuple|None = None, where_dict: dict|None = None, limit: int|None = None) -> list|bool:
    '''
    Возвращает данные из БД
    :param name_table: таблица к которой идет запрос
    :param name_columns_tuple: название запрашиваемых столбцов (<имя столбца>, <имя столбца> ...)
    :param where_dict: условия отбора {<имя столбца>: <значение столбца> ...}
    :param limit: ограничение на количество записей
    :return: [(),()...]
    '''
    table_obj = all_table_dict.get(name_table)
    stmt = select(table_obj)

    if name_columns_tuple:
        stmt = select(*[getattr(table_obj, name) for name in name_columns_tuple])
    if where_dict:
        for name_columns, value_columns in where_dict.items():
            stmt = stmt.where(getattr(table_obj, name_columns) == value_columns)
    if limit:
        stmt = stmt.limit(limit)


    async with async_session() as session:
        if not name_columns_tuple:
            data_by_db = await session.execute(stmt)
            data_by_db = [row for row, in data_by_db.scalars().all()]
        else:
            data_by_db = await session.execute(stmt)
            data_by_db = [row for row in data_by_db.all()]
        return data_by_db



# Создаем асинхронный цикл для выполнения операций
async def main():
    # await create_tables()  # Создаем таблицы, если их нет
    name_table = "stop_work"
    # set_dict = {
    # 'city': 'Липецк',
    # 'object': 'Зверево',
    # 'position': '1',
    # 'queue': '1',
    # 'number_bk': '1',
    # 'cause_stop': 'погода',
    # 'user_id_stop_work': '1234',
    #
    # }
    # post_dict = {'set_dict': set_dict}
    # start_set_time = time.time()
    # for x in range(1, 100001):
    #     await set(name_table, set_dict)
    # end_set_time = time.time()
    # execution_set_time = end_set_time - start_set_time
    # print(f"Время выполнения приложения set: {execution_set_time} секунд")

    name_columns_tuple = ('id', 'city')
    where_dict = {'city': 'Липецк'}
    get_dict = {
    'name_columns_tuple': name_columns_tuple,
    'where_dict': where_dict
    }

    start_get_time = time.time()
    for x in range(1, 1001):
        await get(name_table, name_columns_tuple, where_dict)
        print(x)
    end_get_time = time.time()
    execution_get_time = end_get_time - start_get_time
    print(f"Время выполнения приложения get: {execution_get_time} секунд")




if __name__ == '__main__':
    asyncio.run(main())
