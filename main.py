from jt.finances.stream.spreadsheet_fetcher import fetch_client
from jt.finances.stream import (
    CheckingExtractor, CheckingResultParser, TransactionCollector
)

import sqlite3

# Just testing some stuff.

spreadsheet_id = '1fFmqQOHWJ4n7SjSDFPbGAQnaOYHG2d1V8_679_nDlB0'

collector = TransactionCollector()
fetch_client.fetch_spreadsheet(spreadsheet_id=spreadsheet_id, sheet_range='Budget Log!A1:T150')\
            .map(CheckingExtractor.resolve)\
            .map(CheckingResultParser.resolve)\
            .subscribe(collector)

charges_df = collector.get_charges_df()
charges_df = charges_df.sort_values(by='date')

conn = sqlite3.connect('finances.db')
charges_df.to_sql('CheckingCharges', conn, if_exists='replace')

print('Finished!')
