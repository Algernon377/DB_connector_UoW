from logger.logger_bot import logger


class UnitOfWork:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()
        # logger.error(f'Сработал rollback. Данные не были сохранены в БД \n')

    async def commit(self):
        await self.session.commit()
        await self.session.close()

    async def rollback(self):
        await self.session.rollback()
