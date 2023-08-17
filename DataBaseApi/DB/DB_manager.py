import asyncio
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from .Table_classes import Base


load_dotenv()
POSTGRESQL_URL_FOR_ENGINE = os.getenv('POSTGRESQL_URL_FOR_ENGINE')

engine = create_async_engine(POSTGRESQL_URL_FOR_ENGINE, echo=True)
Base.metadata.create_all(engine)









