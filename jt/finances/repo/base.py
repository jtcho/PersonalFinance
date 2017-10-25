from jt.finances.models import TransactionModel  # noqa: F401


class Repo(object):

    def upsert_transaction_value(self, table_name: str, transaction: TransactionModel) -> None:
        pass


repo = Repo()
