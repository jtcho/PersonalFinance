from pandas import DataFrame    # noqa: F401
from typing import Sequence     # noqa: F401

from pyrsistent import pvector, thaw

import pandas as pd

from jt.finances.models.transaction import Transaction


class Register(object):

    @classmethod
    def initialize_txn_logger(cls):
        return pvector()

    @classmethod
    def charge(cls, charges, date, label, quantity, txn_type):
        return charges.append(Transaction(label=label, quantity=quantity,
                                          date=date, txn_type=txn_type))

    @classmethod
    def pprint(cls, charges):
        print('\n'.join(map(str, charges)))

    @classmethod
    def get_transactions_df(cls, charges):
        # type: (Sequence[Transaction]) -> DataFrame
        serialized = thaw(charges)
        for txn in serialized:
            txn['txn_type'] = txn['txn_type'].value
        return pd.DataFrame(thaw(serialized), columns=['date', 'txn_type', 'label', 'quantity'])
