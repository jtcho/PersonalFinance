from jt.finances.service import service
from jt.finances.stream import (
    CheckingExtractor, ChaseSapphireExtractor, TransactionResultParser, TransactionCollector, TransactionRepoCollector
)
from jt.finances.stream.spreadsheet_fetcher import fetch_client

import sqlite3


def _fetch_transactions(sheet_id, sheet_range, extractor_cls, db_name, table_name, if_exists='replace'):
    """
    Helper method to fetch and store logged transactions.

    :param sheet_id: the ID of the Google Sheet to fetch
    :param sheet_range:  the range to fetch
    :param extractor_cls: the extractor class to stream the sheet rows into
    :param db_name: the database to use
    :param table_name: the table to populate
    :param if_exists: the strategy to use when updating the table
    :return: None
    """
    txn_collector = TransactionCollector(table_name)
    repo_collector = TransactionRepoCollector(table_name)

    fetch_async = fetch_client.fetch_spreadsheet(spreadsheet_id=sheet_id, sheet_range=sheet_range) \
        .map(extractor_cls.resolve) \
        .map(TransactionResultParser.resolve)

    fetch_async.subscribe(txn_collector)
    fetch_async.subscribe(repo_collector)

    charges_df = txn_collector.get_charges_df()
    charges_df = charges_df.sort_values(by='date')
    conn = sqlite3.connect(db_name)
    charges_df.to_sql(table_name, conn, if_exists=if_exists)


def fetch_checking_transactions():
    """
    Fetches and stores transactions for my checking account.
    """
    spreadsheet_id = service.config.spreadsheet_id
    db_name = service.config.db_name
    checking_table = service.config.checking_txns_table
    _fetch_transactions(spreadsheet_id, 'Budget Log!A1:U150', CheckingExtractor, db_name, checking_table)


def fetch_chase_sapphire_transactions():
    """
    Fetches and stores transactions for my Chase Sapphire card.
    """
    spreadsheet_id = service.config.spreadsheet_id
    db_name = service.config.db_name
    chase_sapphire_table = service.config.chase_sapphire_txns_table
    _fetch_transactions(spreadsheet_id, 'Budget Log!A1:U150', ChaseSapphireExtractor, db_name, chase_sapphire_table)
