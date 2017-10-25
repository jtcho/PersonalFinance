from pandas import DataFrame    # noqa: F401
from typing import Sequence     # noqa: F401

from pyrsistent import pvector, thaw

import pandas as pd

from jt.finances.models.transaction import TransactionModel  # noqa: F401


class Register(object):

    @classmethod
    def initialize_txn_logger(cls):
        return pvector()

    @classmethod
    def charge(cls, charges, value):
        return charges.append(value)

    @classmethod
    def pprint(cls, charges):
        print('\n'.join(map(str, charges)))

    @classmethod
    def get_transactions_df(cls, charges: Sequence[TransactionModel]) -> DataFrame:
        serialized = thaw(charges)
        for txn in serialized:
            txn['txn_type'] = txn['txn_type'].value
        return pd.DataFrame(thaw(serialized), columns=['jri', 'date', 'txn_type', 'label', 'quantity'])
