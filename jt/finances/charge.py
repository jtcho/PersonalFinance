from datetime import datetime
from pyrsistent import pvector

import pandas as pd


class Charge(object):

    def __init__(self, date, label, quantity):
        self.label = label
        self.quantity = quantity
        self.date = date or datetime.today()

    def __str__(self):
        return '[{}] {}: {}'.format(self.date.strftime('%m-%d-%Y'), self.label, self.quantity)

    @classmethod
    def to_dict(cls, val):
        return {
            'Label': val.label,
            'Quantity': val.quantity,
            'Date': val.date
        }


class Register(object):

    @classmethod
    def initialize_charge_logger(cls):
        return pvector()

    @classmethod
    def charge(cls, charges, label, quantity, date):
        return charges.append(Charge(label, quantity, date))

    @classmethod
    def pprint(cls, charges):
        print('\n'.join(map(str, charges)))

    @classmethod
    def get_charges_df(cls, charges):
        return pd.DataFrame(list(map(Charge.to_dict, charges)), columns=['Date', 'Label', 'Quantity'])

