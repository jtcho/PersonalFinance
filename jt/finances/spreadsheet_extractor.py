from datetime import datetime
import re

class SpreadsheetCheckingExtractor(object):

    @staticmethod
    def _is_valid_txn_entry(row):
        if row[0]:
            try:
                datetime.strptime(row[0], '%m/%d/%Y')
                return True
            except:
                return False
        return False

    @staticmethod
    def _extract_checking_log(row):
        return (row[0], row[2], row[4])

    @classmethod
    def resolve(cls, values):
        results = []
        for row in values:
            if cls._is_valid_txn_entry(row):
                results.append(cls._extract_checking_log(row))
        return results


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
    def resolve(cls, values):
        return list(map(cls._coerce_row_entry, values))

