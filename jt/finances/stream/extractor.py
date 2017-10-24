from datetime import datetime


class CheckingExtractor(object):

    # noinspection PyBroadException
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
        return {
            'date': row[0],
            'txn_type': row[1],
            'label': row[2],
            'quantity': row[4]
        }

    @classmethod
    def resolve(cls, row):
        if cls._is_valid_txn_entry(row):
            return cls._extract_checking_log(row)
