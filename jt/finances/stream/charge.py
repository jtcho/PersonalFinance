from rx import Observer
from jt.util import logger
from jt.finances.charge import Register

class ChargeCollector(Observer):

    def __init__(self):
        self.charges = Register.initialize_charge_logger()

    def on_next(self, value):
        if value:
            self.charges = Register.charge(self.charges, *value)

    def on_completed(self):
        logger.info('Collected all emissions.')

    def on_error(self, error):
        logger.error('Error occurred while consuming value with message: ' + error.message)

    def get_charges_df(self):
        return Register.get_charges_df(self.charges)

