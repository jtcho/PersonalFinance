from jt.finances.db import CheckingLog
from jt.finances.models import TransactionModel  # noqa: F401
from jt.finances.service import dbsession


class Repo(object):

    def upsert_transaction_value(self, table_name: str, transaction: TransactionModel) -> None:
        # TODO.JT Actually move this into a sub DB repo.
        if table_name == 'CheckingLogs':
            checking_log = dbsession.query(CheckingLog).filter(CheckingLog.jri == transaction.jri).one_or_none()
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
            dbsession.add(checking_log)
            dbsession.flush([checking_log])


repo = Repo()
