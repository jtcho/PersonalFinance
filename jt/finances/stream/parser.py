from datetime import datetime
import re

from jt.finances.models.transaction import TransactionType


class TransactionTypeParser(object):

    @classmethod
    def parse(cls, value):
        try:
            return TransactionType(value)
        except ValueError:
            return TransactionType.UNASSIGNED


class CheckingResultParser(object):
    # noinspection PyBroadException
    @staticmethod
    def _coerce_row_entry(row):
        try:
            txn_date = datetime.strptime(row['date'], '%m/%d/%Y')
            raw_txn_type = row['txn_type']
            txn_type = list(map(TransactionTypeParser.parse, raw_txn_type.split(',')))[0]

            label = row['label']

            txn_quantity = row['quantity']
            groups = re.findall('\d*\.\d*', row['quantity'])
            if '(' in txn_quantity:
                txn_quantity = -1 * float(groups[0])
            else:
                txn_quantity = float(groups[0])

            return {
                'date': txn_date,
                'txn_type': txn_type,
                'label': label,
                'quantity': txn_quantity
            }
        except:
            return None

    @classmethod
    def resolve(cls, value):
        return cls._coerce_row_entry(value)
