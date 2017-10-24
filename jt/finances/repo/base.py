from jt.finances.models import Transaction  # noqa: F401


class Repo(object):

    def upsert_transaction_value(self, table_name: str, transaction: Transaction) -> None:
        pass


repo = Repo()
