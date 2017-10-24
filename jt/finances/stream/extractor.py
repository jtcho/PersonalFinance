from datetime import datetime


class Extractor(object):

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


class CheckingExtractor(Extractor):

    @staticmethod
    def _extract_txn_log(row):
        return {
            'jri': row[-1],
            'date': row[0],
            'txn_type': row[1],
            'label': row[2],
            'quantity': row[4]
        }

    @classmethod
    def resolve(cls, row):
        if cls._is_valid_txn_entry(row):
            return cls._extract_txn_log(row)


class ChaseSapphireExtractor(Extractor):

    @staticmethod
    def _extract_txn_log(row):
        return {
            'jri': row[-1],
            'date': row[0],
            'txn_type': row[1],
            'label': row[2],
            'quantity': row[7]
        }

    @classmethod
    def resolve(cls, row):
        if cls._is_valid_txn_entry(row):
            return cls._extract_txn_log(row)
