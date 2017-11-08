from jt.finances.db.base import BaseMixin, Base
from jt.finances.models import TransactionModel  # noqa: F401
from jt.finances.models.transaction import TransactionType

from sqlalchemy import Column, Text, Float, Date, Enum
from typing import Any as TbdType


class CheckingLog(Base, BaseMixin):

    __tablename__ = 'CheckingLogs'

    label = Column('label', Text, nullable=False)
    quantity = Column('quantity', Float, nullable=False)
    date = Column('date', Date, nullable=False)
    txn_type = Column('txn_type', Enum(TransactionType), nullable=False)

    @classmethod
    def upsert_transaction_value(cls, session: TbdType, transaction: TransactionModel):
        checking_log = session.query(CheckingLog)\
                              .filter(CheckingLog.jri == transaction.jri)\
                              .one_or_none()
        if checking_log:
            checking_log.label = transaction.label
            checking_log.quantity = transaction.quantity
            checking_log.date = transaction.date
            checking_log.txn_type = transaction.txn_type
        else:
            checking_log = CheckingLog(jri=transaction.jri,
                                       label=transaction.label,
                                       quantity=transaction.quantity,
                                       date=transaction.date,
                                       txn_type=transaction.txn_type)
        session.add(checking_log)
        session.flush([checking_log])
