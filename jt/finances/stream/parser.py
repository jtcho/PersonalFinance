from datetime import datetime
import re


class CheckingResultParser(object):

    @staticmethod
    def _coerce_row_entry(row):
        try:
            txn_date = datetime.strptime(row[0], '%m/%d/%Y')
            desc = row[1]
            txn_quantity = row[2]
            groups = re.findall('\d*\.\d*', row[2])
            if '(' in txn_quantity:
                txn_quantity = -1 * float(groups[0])
            else:
                txn_quantity = float(groups[0])
            return txn_date, desc, txn_quantity
        except:
            return None

    @classmethod
    def resolve(cls, value):
        return cls._coerce_row_entry(value)

