from rx import Observer
from jt.util import logger
from jt.finances.charge import Register


class TransactionCollector(Observer):
    """ Collects all """

    def __init__(self):
        self.transactions = Register.initialize_txn_logger()

    def on_next(self, value):
        if value:
            self.transactions = Register.charge(self.transactions, **value)

    def on_completed(self):
        logger.info('Collected all emissions.')

    def on_error(self, error):
        logger.error('Error occurred while consuming value with message: ' + error.message)

    def get_charges_df(self):
        return Register.get_transactions_df(self.transactions)
