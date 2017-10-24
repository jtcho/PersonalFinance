#! /usr/bin/env python

from jt.finances import handler

handler.fetch_checking_transactions()
handler.fetch_chase_sapphire_transactions()

print('Exited successfully.')
