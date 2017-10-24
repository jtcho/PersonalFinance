from rx import Observer

from jt.finances.repo.base import repo
from jt.util import logger
from jt.finances.register import Register


class TransactionCollector(Observer):
    """ Collects all transactions from a stream into a list. """

    __name__ = 'TransactionCollector'

    def __init__(self, label):
        self.transactions = Register.initialize_txn_logger()
        self.label = label

    def on_next(self, value):
        if value:
            self.transactions = Register.charge(self.transactions, value)

    def on_completed(self):
        logger.info('[{}] Collected all emissions for {}.'.format(self.__name__, self.label))

    def on_error(self, error):
        logger.error('Error occurred while consuming value with message: ' + error.message)

    def get_charges_df(self):
        return Register.get_transactions_df(self.transactions)


class TransactionRepoCollector(Observer):

    __name__ = 'TransactionRepoCollector'

    def __init__(self, table_name):
        self.table_name = table_name

    def on_next(self, transaction):
        if transaction:
            repo.upsert_transaction_value(self.table_name, transaction)

    def on_completed(self):
        logger.info('[{}] Collected all emissions for {}.'.format(self.__name__, self.table_name))

    def on_error(self, error):
        logger.error('Error occurred while consuming value with message: ' + error.message)
