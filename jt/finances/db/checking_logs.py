from jt.finances.db.base import ModelBase
from jt.finances.models.transaction import TransactionType

from sqlalchemy import Column, Text, Float, Date, Enum


class CheckingLogs(ModelBase):
    label = Column('label', Text)
    quantity = Column('quantity', Float)
    date = Column('date', Date)
    txn_type = Column('txn_type', Enum(TransactionType))
