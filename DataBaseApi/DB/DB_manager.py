import asyncio
import os
from dotenv import load_dotenv


from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from .Table_classes import Base, all_table_dict

from logger.logger_bot import logger


load_dotenv()
POSTGRESQL_URL_FOR_ENGINE = os.getenv('POSTGRESQL_URL_FOR_ENGINE')

engine = create_engine(POSTGRESQL_URL_FOR_ENGINE, echo=True)

try:
    Base.metadata.create_all(engine)
except Exception as ex:
    logger.error(f'connect from DB error\n{ ex}')
    print(f'connect from DB error\n{ ex}')




Session = sessionmaker(bind=engine)

new_user = all_table_dict.get('users')(**{'user_id':'110000011', 'username':'alex'})
ses = Session()
# with Session() as session:
#     session.add(new_user)
#     session.commit()
    # res = session.query(UsersTable).all()
    # # res = session.execute(select(UsersTable)).all()
    # print(res)
    # session.add(new_user)
    # session.commit()
    # logger.warning(f"Метод insert")

class DB_connector:


    # @staticmethod
    # def return_name_columns(name_table: str)-> tuple(str):
    #     return tuple(all_table_dict.get(name_table).__annotations__)



    @staticmethod
    def set(name_table: str, set_dict: dict) -> bool:
        '''
        записывает новую строку в таблицу <name_table>
        :param name_table: имя таблицы куда записываем
        :param set_dict: dict формата {<имя столбца>:<значение столбца>,<имя столбца>:<значение столбца>}
        :return:
        '''
        new_row = all_table_dict.get(name_table)(**set_dict)
        try:
            with Session() as session:
                session.add(new_row)
                session.query(all_table_dict.get(name_table))
                session.commit()
                return True
        except Exception as ex:
            logger.error(f'data did not save from DB\n{ex}')
            print(f'data did not save from DB\n{ex}')
            return False


    @staticmethod
    def set_many(name_table: str, set_many_list: list[dict], group_write: bool = True) -> bool:
        '''
        Создает список обьектов и добавляет транзакциями по 10 000 записей
        если выставлен флаг group_write в положении False - добавляет по одной записи(сильно замедляет работу)
        :param name_table: имя таблицы в которую добавляем запись
        :param request_list: список dicts [{<имя столбца>:<значение столбца>,<имя столбца>:<значение столбца>},...]
        :param group_write: при положении True формирует транзакции по 10 000 записей, при False - записывает по одной.
        :return: True - при успешной транзакции, False - при ошибке добавления
        '''

        def save_batch(rows_dict):
            try:
                with Session() as session:
                    session.add_all(list(rows_dict.values()))
                    session.commit()
                return True
            except Exception as ex:
                logger.error(f'data did not save from DB\n{ex}')
                return False


        if group_write:
            table_obj = all_table_dict.get(name_table)
            new_rows_dict = {}
            num_iter = 0
            for request_dict in set_many_list:
                num_iter += 1
                new_rows_dict[str(num_iter)] = table_obj(**request_dict)
                if num_iter > 10000:
                    if not save_batch(new_rows_dict):
                        return False
                    new_rows_dict = {}
                    num_iter = 0
            if not save_batch(new_rows_dict):
                return False
            return True
        else:
            table_obj = all_table_dict.get(name_table)
            new_rows_list = [table_obj(**request_dict) for request_dict in set_many_list]
            for row in new_rows_list:
                DB_connector.set(name_table, row)

    @staticmethod
    def get(name_table: str,
            name_columns_tuple: tuple|None = None,
            where_dict: dict|None = None,
            limit: int|None = None) -> list|bool:
        '''

        :param name_table:
        :param name_columns_tuple:
        :param where_dict:
        :return:
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

        try:
            with Session() as session:
                if not name_columns_tuple:
                    data_by_db = session.scalars(stmt).all()
                else:
                    data_by_db = session.execute(stmt).all()
                return data_by_db
        except Exception as ex:
            logger.error(f'data did not save from DB\n{ex}')
            print(f'data did not save from DB\n{ex}')
            return False



    @staticmethod
    def update(name_table: str,
            update_columns_dict: dict,
            where_dict: dict|None = None) -> bool:
        '''
        обновляет данные в БД если переданные параметры верны. where_dict - критерии поиска
        :param name_table: имя таблицы в которой находятся данные
        :param update_columns_dict: {<имя изменяемого столбца>:<новое значение столбца>,
                                    <имя изменяемого столбца>:<новое значение столбца>}
        :param where_dict:{<имя столбца>:<значение столбца>}
        :return: bool
        '''

        rows_list = DB_connector.get(name_table=name_table,
                                            where_dict=where_dict)
        update_rows_list = []
        for row in rows_list:
            for name_column, value_column in update_columns_dict.items():
                setattr(row, name_column, value_column)
                update_rows_list.append(row)
            # update_rows_list = [getattr(row, name_column) == value_column for row in rows_list]
        if not update_rows_list:
            return False

        try:
            with Session() as session:
                session.add_all(update_rows_list)
                session.commit()
                return True
        except Exception as ex:
            logger.error(f'data did not save from DB\n{ex}')
            print(f'data did not save from DB\n{ex}')
            return False





# request_dict = {'username': 'aleksa'}
# where_dict = {'user_id': '1211112'}
# name_table = 'users'
#
# data = DB_connector.update(name_table, request_dict, where_dict=where_dict)
# print(data)
