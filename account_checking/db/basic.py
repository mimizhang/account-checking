# -*- coding: utf-8 -*-

import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..settings import *


def get_engine():
    connect_str = '{}+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        DB_TYPE, USER, PWD,
        HOST, PORT, DB
    )
    engine = create_engine(connect_str, encoding='utf-8')
    return engine


engine = get_engine()
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
db_session = DBSession()
metadata = MetaData(engine)


__all__ = ['engine', 'Base', 'db_session', 'metadata']
