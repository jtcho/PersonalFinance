from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import Index
from sqlalchemy.ext.declarative import declarative_base, declared_attr

Base = declarative_base()


class BaseMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column('id', Integer, primary_key=True)
    jri = Column('jri', String(16), nullable=False)

    Index('idx_jri', 'jri', unique=True)
