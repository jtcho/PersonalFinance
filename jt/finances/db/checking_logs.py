from jt.finances.db.base import BaseMixin, Base
from jt.finances.models.transaction import TransactionType

from sqlalchemy import Column, Text, Float, Date, Enum


class CheckingLog(Base, BaseMixin):

    __tablename__ = 'CheckingLogs'

    label = Column('label', Text, nullable=False)
    quantity = Column('quantity', Float, nullable=False)
    date = Column('date', Date, nullable=False)
    txn_type = Column('txn_type', Enum(TransactionType), nullable=False)
