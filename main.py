from jt.finances.stream.spreadsheet_fetcher import fetch_client
from jt.finances.stream import (
            CheckingExtractor, CheckingResultParser, ListCollector, ChargeCollector
        )
from jt.finances.charge import Register

import sqlite3

# Just testing some stuff.

collector = ChargeCollector()
fetch_client.fetch_spreadsheet(sheet_range='Budget Log!A1:T150')\
            .map(CheckingExtractor.resolve)\
            .map(CheckingResultParser.resolve)\
            .subscribe(collector)

charges_df = collector.get_charges_df()
charges_df = charges_df.sort_values(by='Date')

conn = sqlite3.connect('finances.db')
charges_df.to_sql('CheckingCharges', conn, if_exists='replace')

print('Finished!')

