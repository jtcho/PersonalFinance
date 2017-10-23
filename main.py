from jt.finances.spreadsheet_fetcher import fetch_client
from jt.finances.spreadsheet_extractor import SpreadsheetCheckingExtractor, CheckingResultParser
from jt.finances.charge import Register

import sqlite3

# Just testing some stuff.

raw_result = fetch_client.fetch_spreadsheet(sheet_range='Budget Log!A1:T150')
result = SpreadsheetCheckingExtractor.resolve(raw_result)
result = CheckingResultParser.resolve(result)

charges = Register.initialize_charge_logger()
for charge in result:
    if charge:
        charges = Register.charge(charges, *charge)
charges_df = Register.get_charges_df(charges)
charges_df = charges_df.sort_values(by='Date')

conn = sqlite3.connect('finances.db')
charges_df.to_sql('CheckingCharges', conn, if_exists='replace')

import ipdb; ipdb.set_trace()
print('Fin')

