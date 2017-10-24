from datetime import datetime
import re
from typing import Optional, Mapping  # noqa: F401

from jt.finances.models.transaction import TransactionType, Transaction


class TransactionTypeParser(object):

    @classmethod
    def parse(cls, value):
        try:
            return TransactionType(value)
        except ValueError:
            return TransactionType.UNASSIGNED


class TransactionResultParser(object):

    # noinspection PyBroadException
    @staticmethod
    def _coerce_row_entry(row: Mapping[str, str]) -> Optional[Transaction]:
        charge_pattern = '[\d]*\.[\d]*'
        try:
            jri = row['jri'].split('-')[0]  # Temporarily reduce the amount of entropy.
            txn_date = datetime.strptime(row['date'], '%m/%d/%Y').date()
            raw_txn_type = row['txn_type']
            txn_type = [TransactionTypeParser.parse(val) for val in raw_txn_type.split(',')][0]

            label = row['label']

            quantity = row['quantity']
            groups = re.findall(charge_pattern, row['quantity'].replace(',', ''))
            if '(' in quantity:
                txn_quantity = -1 * float(groups[0])
            else:
                txn_quantity = float(groups[0])

            return Transaction(
                jri=jri,
                date=txn_date,
                label=label,
                quantity=txn_quantity,
                txn_type=txn_type
            )
        except:
            return None

    @classmethod
    def resolve(cls, value: Mapping[str, str]) -> Optional[Transaction]:
        return cls._coerce_row_entry(value)
