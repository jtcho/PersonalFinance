from abc import ABCMeta, abstractmethod, abstractproperty

from jt.finances.db.checking_logs import CheckingLog
from jt.finances.models import TransactionModel  # noqa: F401
from jt.finances.service import dbsession


class FinanceRepo(object):

    __metaclass__ = ABCMeta

    @abstractproperty
    def session(self):
        raise NotImplementedError

    @abstractmethod
    def upsert_transaction_value(self, table_name: str, transaction: TransactionModel) -> None:
        raise NotImplementedError


class FinanceDBRepo(FinanceRepo):

    def __init__(self):
        self._session = dbsession

    @property
    def session(self):
        return self._session

    def upsert_transaction_value(self, table_name: str, transaction: TransactionModel) -> None:
        if table_name == 'CheckingLogs':
            CheckingLog.upsert_transaction_value(self.session, transaction)
