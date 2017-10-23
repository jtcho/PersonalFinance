from datetime import datetime


class CheckingExtractor(object):

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
    def resolve(cls, row):
        if cls._is_valid_txn_entry(row):
            return cls._extract_checking_log(row)

