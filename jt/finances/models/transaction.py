from datetime import datetime
from enum import Enum

from pyrsistent import PRecord, field


class Model(PRecord):
    pass


class TransactionType(Enum):
    DEBT = 'Debt'
    FOOD = 'Food'
    TRANSPORT = 'Transport'
    RECREATION = 'Recreation'
    RENT = 'Rent'
    LUXURY = 'Luxury'
    SUPPLIES = 'Supplies'
    SUBSCRIPTION = 'Subscription'
    PAY = 'Pay'
    UNASSIGNED = 'Unassigned'


class Transaction(Model):
    __version__ = '1.0'

    label = field(type=str, mandatory=True)
    quantity = field(type=float, mandatory=True)
    date = field(type=datetime, mandatory=True, initial=datetime.now())
    txn_type = field(type=TransactionType, mandatory=True, initial=TransactionType.UNASSIGNED)

    def __str__(self):
        return '[{}] {}: {}'.format(self.date.strftime('%m-%d-%Y'), self.label, self.quantity)
