from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ModelBase(Base):
    id = Column('id', Integer, primary_key=True)
    jri = Column('jri', String(16))

    def __init__(self):
        self.__tablename__ = self.__class__.__name__
