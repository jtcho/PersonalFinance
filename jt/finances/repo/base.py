from jt.finances.models import TransactionModel  # noqa: F401
from jt.finances.repo.api import FinanceRepo, FinanceDBRepo

from contextlib import contextmanager


class Repo(object):

    _instance = None  # type: FinanceRepo

    def set_impl(self, repo_impl):
        self._instance = repo_impl

    @contextmanager
    def transaction_context(self):
        yield
        self._instance.session.commit()

    def transaction(self, func_):
        def wrap_with_txn_context(*args, **kwargs):
            with self.transaction_context():
                func_(*args, **kwargs)
        return wrap_with_txn_context

    def upsert_transaction_value(self, table_name: str, transaction: TransactionModel) -> None:
        self._instance.upsert_transaction_value(table_name, transaction)


repo = Repo()
transaction = repo.transaction
repo.set_impl(FinanceDBRepo())
